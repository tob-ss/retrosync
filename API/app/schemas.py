from pydantic import BaseModel

class LocalMetadataBase(BaseModel):
    GameID: str
    GameName: str
    LastModified: float
    DeviceID: str

class LocalMetadataCreate(LocalMetadataBase):
    pass

class LocalMetadata(LocalMetadataBase):
    GameID: str

    class Config:
        orm_mode = True