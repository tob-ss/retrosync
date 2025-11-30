from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_metadata, create_dynamic_syncrequests
import models, schemas, crud
from sqlalchemy.orm import Session
from classes import LocalMetadataProcessor as LMP, SyncRequestProcessor as SRP, DupeCloudMDRemover as DCR

app = FastAPI()

MetadataModel = create_dynamic_metadata("test")
SyncRequestModel = create_dynamic_syncrequests("test")


Base.metadata.create_all(bind=engine)



@app.post("/metadata/append", response_model=schemas.Metadata)
def create_metadata(metadata: schemas.MetadataCreate, db: Session = Depends(get_db)):
    print(metadata.LID)
    delete_dupes = DCR(db, metadata.LID)
    append_LMD = LMP(db, metadata)
    return delete_dupes.delete_dupe_games()
    #return append_LMD.append_metadata()

@app.post("/sync/append", response_model=schemas.SyncRequests)
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