from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_localmetadata, create_dynamic_uploadrequest, create_dynamic_downloadrequest
import models, schemas, crud
from sqlalchemy.orm import Session

class LocalMetadataProcessor:
    def __init__(self, JSON):
        self.JSON = JSON

    def print_LMD(self): 
        print(f"I got the JSON {self.JSON}")

    def append_LMD(localmetadata: schemas.MetadataCreate, db: Session = Depends(get_db)):
        return crud.create_metadata(db, localmetadata)