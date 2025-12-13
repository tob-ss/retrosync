from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_syncrequests
import models, schemas, crud
from sqlalchemy.orm import Session
from decimal import Decimal, getcontext
import time
import hashlib

class LocalMetadataProcessor:
    def __init__(self, db: Session, localmetadata: schemas.MetadataCreate):
        self.localmetadata = localmetadata
        self.db = db

    def hash_generator(self):
        m = hashlib.sha256()
        m.update(bytes(self.localmetadata.GameID), encoding='utf-8')
        m.update(bytes(self.localmetadata.LastModified), encoding='utf-8')
        m.update(bytes(self.localmetadata.DeviceID), encoding='utf-8')
        return m.hexdigest()

    def append_metadata(self):
        md_hash = self.hash_generator()
        if self.localmetadata.LID == "CL":
            delete_dupes = DupeCloudMDRemover(db=self.db, LID=self.localmetadata.LID, GameID=self.localmetadata.GameID, LastModified=self.localmetadata.LastModified, DeviceID=self.localmetadata.DeviceID)
            delete_dupes.get_gamesby_LID()
            return crud.create_metadata_cloud(self.db, self.localmetadata, hash=md_hash)
        else:
            return crud.create_metadata(self.db, self.localmetadata, hash=md_hash)
        
class LocalMetadataFlusher:
    def __init__(self, db: Session, DeviceID: str):
        self.DeviceID = DeviceID
        self.db = db

    def flush_metadata(self):
        from main import MetadataModel
        #print(f"{MetadataModel.LID} and {MetadataModel.DeviceID}")
        db_localmetadata = self.db.query(MetadataModel).filter(MetadataModel.LID == "L").all()
        #print(MetadataModel.LID)
        for x in db_localmetadata:
            if x.LID == "L" and x.DeviceID == self.DeviceID:
                print("debug0")
                self.db.delete(x)
                self.db.commit()
                
            else:
                continue
        return {"DeviceID": "Just work bruv"}

class SyncRequestProcessor:
    def __init__(self, db: Session, syncrequest: schemas.SyncRequestsCreate):
        self.syncrequest = syncrequest
        self.db = db

    def append_syncrequest(self):
        return crud.create_syncrequest(self.db, self.syncrequest)
    
class DupeCloudMDRemover:
    def __init__(self, db: Session, LID: str, GameID: str, LastModified: Decimal, DeviceID: str):
        self.db = db
        self.LID = LID
        self.GameID = GameID
        self.LastModified = LastModified.quantize(Decimal('0.000000'))
        self.DeviceID = DeviceID

    def get_gamesby_LID(self):
        from main import MetadataModel
        LID_table = self.db.query(MetadataModel).filter(MetadataModel.LID == self.LID).all()
        for x in LID_table:
            if x.LID == "CL" and x.GameID == self.GameID and x.LastModified == self.LastModified and x.DeviceID == self.DeviceID:
                self.db.delete(x)
                self.db.commit()
            else: 
                continue

class DaemonStatusChecker:
    def __init__(self, db: Session, DeviceID: str):
        self.DeviceID = DeviceID
        self.db = db

    def get_daemon_status(self):
        from main import DaemonStatusModel
        db_daemonstatus = self.db.query(DaemonStatusModel).filter(DaemonStatusModel.DeviceID == self.DeviceID).first()
        if db_daemonstatus == None:
            return 0
        self.db.commit()
        self.db.refresh(db_daemonstatus)
        LastOnline = db_daemonstatus.LastOnline
        return LastOnline
    
    def online_calculator(self):
        x = 0
        LastOnline1 = self.get_daemon_status()
        if LastOnline1 == 0:
            return 0
        while x <= 24:
            x += 1
            time.sleep(5)
            LastOnline2 = self.get_daemon_status()
            print(LastOnline2)
            if LastOnline1 == LastOnline2:
                pass
            else:
                return 1
        print(f"Last Online 1 was {LastOnline1} and Last Online 2 was {LastOnline2}")
        return 0
    

class SyncCompletionChecker:
    def __init__(self, db: Session, DeviceID: str):
        self.db = db
        self.DeviceID = DeviceID

    def completion_checker(self):
        from main import SyncRequestModel
        Device_table = self.db.query(SyncRequestModel).filter(SyncRequestModel.DeviceID == self.DeviceID).all()
        for x in Device_table:
            if x.Completed == False:
                if x.GameID == "ALL":
                    return {"GameID": "ALL", "Operation": x.Operation}
                else:
                    return {"GameID": x.GameID, "Operation": x.Operation}
            if x.Completed == True:
                pass
