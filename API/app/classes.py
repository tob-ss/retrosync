from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_uploadrequest, create_dynamic_downloadrequest
import models, schemas, crud
from sqlalchemy.orm import Session

class LocalMetadataProcessor:
    def __init__(self, localmetadata: schemas.MetadataCreate, db: Session = Depends(get_db)):
        self.localmetadata = localmetadata
        self.db = db

    def print_LMD(self): 
        print(f"I got the JSON {self.localmetadata}")

    def append_LMD(self):
        return crud.create_metadata(self.db, self.localmetadata)