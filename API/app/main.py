from typing import Union
from fastapi import FastAPI, HTTPException, Depends, Request, status
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_syncrequests, create_dynamic_daemonstatus
import models, schemas, crud
from sqlalchemy.orm import Session
from classes import LocalMetadataProcessor as LMP, SyncRequestProcessor as SRP, DupeCloudMDRemover as DCR, LocalMetadataFlusher as LMF, DaemonStatusChecker as DSC, SyncCompletionChecker as SCC

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MetadataModel = create_dynamic_metadata("test")
SyncRequestModel = create_dynamic_syncrequests("test")
DaemonStatusModel = create_dynamic_daemonstatus("test")

Base.metadata.create_all(bind=engine)

@app.post("/metadata/append/", response_model=schemas.Metadata)
def create_metadata(metadata: schemas.MetadataCreate, db: Session = Depends(get_db)):
    Base.metadata.create_all(bind=engine)
    Create_Table = MetadataModel()
    append_LMD = LMP(db, metadata)
    return append_LMD.append_metadata()

#@app.get("/metadata/fetch", response_model=)

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
    try:
        append_SR = SRP(db, syncrequest)
        return append_SR.append_syncrequest()
    except Exception:
        raise HTTPException(status_code=405, detail=f"No idea wtf happened ngl, heres the body of the request {syncrequest}")

@app.get("/sync/status/")
def get_sync_completion(DeviceID: str, db: Session = Depends((get_db))):
    get_completion = SCC(db, DeviceID)
    return get_completion.completion_checker()

@app.post("/daemon/status/", response_model=schemas.DaemonStatus)
def create_daemonstatus(daemonstatus: schemas.DaemonStatusCreate, db: Session = Depends(get_db)):
    return crud.create_daemonstatus(db, daemonstatus)

@app.get("/daemon/status/")
def get_daemonstatus(DeviceID: str, db: Session = Depends((get_db))):
    get_status = DSC(db, DeviceID)
    return get_status.online_calculator()


                     

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