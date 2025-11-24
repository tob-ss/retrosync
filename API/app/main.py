from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, get_db
from models import create_dynamic_localmetadata
import models, schemas, crud
from sqlalchemy.orm import Session

app = FastAPI()

LocalMetadataModel = create_dynamic_localmetadata("test")

Base.metadata.create_all(bind=engine)

@app.post("/metadata/", response_model=schemas.LocalMetadata)
def create_localmetadata(localmetadata: schemas.LocalMetadataCreate, db: Session = Depends(get_db)):
    #print(f"Got: {localmetadata.LastModified}")
    return crud.create_localmetadata(db, localmetadata)

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