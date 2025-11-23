from typing import Union
from fastapi import FastAPI, HTTPException
from backend import connect, create_metadata

app = FastAPI()
conn = connect()
cursor = conn.cursor()

@app.post("/metadata/")
async def add_metadata(game: dict):
    rowcount = create_metadata(game)
    if rowcount > 0:
        return {"Successfully Uploaded Metadata": game}
    else:
        raise HTTPException(status_code=400, detail="Metadata not added")