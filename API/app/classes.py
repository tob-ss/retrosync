from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_syncrequests
import models, schemas, crud
from sqlalchemy.orm import Session
from decimal import Decimal

class LocalMetadataProcessor:
    def __init__(self, db: Session, localmetadata: schemas.MetadataCreate):
        self.localmetadata = localmetadata
        self.db = db

    def append_metadata(self):
        if self.localmetadata.LID == "CL":
            return crud.create_metadata_cloud(self.db, self.localmetadata)
        else:
            return crud.create_metadata(self.db, self.localmetadata)
            
class SyncRequestProcessor:
    def __init__(self, db: Session, syncrequest: schemas.SyncRequestsCreate):
        self.syncrequest = syncrequest
        self.db = db

    def append_syncrequest(self):
        return crud.create_syncrequest(self.db, self.syncrequest)
    
class DupeCloudMDRemover:
    def __init__(self, db: Session, LID: str, GameID: str, LastModified: Decimal):
        self.db = db
        self.LID = LID
        self.GameID = GameID
        self.LastModified = LastModified

    def get_gamesby_LID(self):
        from main import MetadataModel
        LID_table = self.db.query(MetadataModel).filter(MetadataModel.LID == self.LID).all()
        for x in LID_table:
            duplicate_row = self.db.query(MetadataModel).filter(x.GameID == self.GameID, x.LastModified == self.LastModified).first()
            if duplicate_row:
                print("I would delete a dupe record now!")
                self.db.delete(duplicate_row)
            else:
                continue
            #for x in lid table, if self.db.query(x).filter(x.gameid == self.gameid, x.lastmod == self.lastmod). maybe .first()? if not do a second loop with .all()
            self.db.commit()
        #return LID_table
    #def delete_dupe_games(self):
    #    print(self.get_gamesby_LID())