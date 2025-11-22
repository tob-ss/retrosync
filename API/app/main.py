from typing import Union
from fastapi import FastAPI, HTTPException
from backend import connect, create_metadata

app = FastAPI()
conn = connect()
cursor = conn.cursor()

@app.post("/metadata/")
async def add_metadata(device: str, game: dict):
    post_id = create_metadata(device, game)
    if post_id:
        return {"id": post_id, "device": device, "save metadata": game}
    else:
        raise HTTPException(status_code=400, detail="Metadata not added")