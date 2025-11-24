from pydantic import BaseModel

class LocalMetadataBase(BaseModel):
    gameID: str
    gameName: str
    LastModified: float
    DeviceID: str

class LocalMetadataCreate(LocalMetadataBase):
    pass

class LocalMetadata(LocalMetadataBase):
    gameID: str

    class Config:
        orm_mode = True