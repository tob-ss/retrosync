from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_syncrequests
import models, schemas, crud
from sqlalchemy.orm import Session
from decimal import Decimal, getcontext

class LocalMetadataProcessor:
    def __init__(self, db: Session, localmetadata: schemas.MetadataCreate):
        self.localmetadata = localmetadata
        self.db = db

    def append_metadata(self):
        if self.localmetadata.LID == "CL":
            delete_dupes = DupeCloudMDRemover(db=self.db, LID=self.localmetadata.LID, GameID=self.localmetadata.GameID, LastModified=self.localmetadata.LastModified, DeviceID=self.localmetadata.DeviceID)
            delete_dupes.get_gamesby_LID()
            return crud.create_metadata_cloud(self.db, self.localmetadata)
        else:
            return crud.create_metadata(self.db, self.localmetadata)
        
class LocalMetadataFlusher:
    def __init__(self, db: Session, DeviceID: str):
        self.DeviceID = DeviceID
        self.db = db

    def flush_metadata(self):
        from main import MetadataModel
        #print(f"{MetadataModel.LID} and {MetadataModel.DeviceID}")
        db_localmetadata = self.db.query(MetadataModel).filter(MetadataModel.LID == "L", MetadataModel.DeviceID == self.DeviceID).all()
        if db_localmetadata is not None:
            for x in db_localmetadata:
                if x.LID == "L" and x.DeviceID == self.DeviceID:
                    self.db.delete(x)
                    self.db.commit()
                else: 
                    continue
        else:
            pass

            
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
            #print(f"full information comparison on current row: ID: {x.ID}, row LID: {x.LID} vs passed LID: {self.LID}, GameID: {x.GameID} vs passed GameID: {self.GameID}, row GameName: {x.GameName}, row LastMod: {x.LastModified} vs passed LastMod: {self.LastModified}")
            #for x in lid table, if self.db.query(x).filter(x.gameid == self.gameid, x.lastmod == self.lastmod). maybe .first()? if not do a second loop with .all()
            
        #return LID_table
    #def delete_dupe_games(self):
    #    print(self.get_gamesby_LID())