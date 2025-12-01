from typing import Union
from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_syncrequests
import models, schemas, crud
from sqlalchemy.orm import Session
from classes import LocalMetadataProcessor as LMP, SyncRequestProcessor as SRP, DupeCloudMDRemover as DCR, LocalMetadataFlusher as LMF

app = FastAPI()

MetadataModel = create_dynamic_metadata("test")
SyncRequestModel = create_dynamic_syncrequests("test")


Base.metadata.create_all(bind=engine)

@app.post("/metadata/append/", response_model=schemas.Metadata)
def create_metadata(metadata: schemas.MetadataCreate, db: Session = Depends(get_db)):
    Base.metadata.create_all(bind=engine)
    Create_Table = MetadataModel()
    append_LMD = LMP(db, metadata)
    return append_LMD.append_metadata()

@app.post("/metadata/delete/localflush/", response_model=schemas.Metadata_Device)
def flush_localmetadata(DeviceID: str, db: Session = Depends(get_db)):
    try:
        print(DeviceID)
        flush_LMD = LMF(db, DeviceID)
        return flush_LMD.flush_metadata()
    except Exception:
        raise HTTPException(status_code=406, detail="New Error Found")

@app.post("/sync/append/", response_model=schemas.SyncRequests)
def create_syncrequest(syncrequest: schemas.SyncRequestsCreate, db: Session = Depends(get_db)):
    append_SR = SRP(db, syncrequest)
    return append_SR.append_syncrequest()

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