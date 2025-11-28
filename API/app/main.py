from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_uploadrequest, create_dynamic_downloadrequest
import models, schemas, crud
from sqlalchemy.orm import Session
from classes import LocalMetadataProcessor as LMP

app = FastAPI()

MetadataModel = create_dynamic_metadata("test")
UploadRequestModel = create_dynamic_uploadrequest("test")
DownloadRequestModel = create_dynamic_downloadrequest("test")

Base.metadata.create_all(bind=engine)

append_LMD = LMP.append_LMD

@app.post("/metadata/", response_model=schemas.Metadata)
def create_metadata(metadata: schemas.MetadataCreate, db: Session = Depends(get_db)):
    
    return crud.create_metadata(db, metadata)

@app.post("/upload/", response_model=schemas.UploadRequest)
def create_uploadrequest(uploadrequest: schemas.UploadRequestCreate, db: Session = Depends(get_db)):
    return crud.create_uploadrequest(db, uploadrequest)

@app.post("/download/", response_model=schemas.DownloadRequest)
def create_downloadrequest(downloadrequest: schemas.DownloadRequestCreate, db: Session = Depends(get_db)):
    return crud.create_downloadrequest(db, downloadrequest)

#@app.post("/daemon/", response_model=schemas.DaemonStatus)
#def create_daemonstatus(daemonstatus: schemas.DaemonStatusCreate, db: Session = Depends(get_db)):
#    return crud.create_daemonstatus(db, daemonstatus)

"""

conn = connect()
cursor = conn.cursor()

@app.post("/metadata/")
async def add_metadata(game: dict):
    post_id = create_metadata(game)
    flush_duplicates()
    if post_id:
        return {"Successfully Uploaded Metadata": game}
    else:
        print(post_id)
        raise HTTPException(status_code=400, detail="Metadata not added")

"""