from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_localmetadata, create_dynamic_uploadrequest, create_dynamic_downloadrequest
import models, schemas, crud
from sqlalchemy.orm import Session

app = FastAPI()

LocalMetadataModel = create_dynamic_localmetadata("test")
UploadRequestModel = create_dynamic_uploadrequest("test")
DownloadRequestModel = create_dynamic_downloadrequest("test")

Base.metadata.create_all(bind=engine)

@app.post("/metadata/", response_model=schemas.LocalMetadata)
def create_localmetadata(localmetadata: schemas.LocalMetadataCreate, db: Session = Depends(get_db)):
    #print(f"Got: {localmetadata.LastModified}")
    return crud.create_localmetadata(db, localmetadata)

@app.post("/upload/", response_model=schemas.UploadRequest)
def create_uploadrequest(uploadrequest: schemas.UploadRequestCreate, db: Session = Depends(get_db)):
    return crud.create_uploadrequest(db, uploadrequest)

@app.post("/download/", response_model=schemas.DownloadRequest)
def create_downloadrequest(downloadrequest: schemas.DownloadRequestCreate, db: Session = Depends(get_db)):
    return crud.create_downloadrequest(db, downloadrequest)

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