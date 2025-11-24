from pydantic import BaseModel
from decimal import Decimal

class LocalMetadataBase(BaseModel):
    GameID: str
    GameName: str
    LastModified: str
    DeviceID: str

class LocalMetadataCreate(LocalMetadataBase):
    pass

class LocalMetadata(LocalMetadataBase):
    GameID: str

    class Config:
        orm_mode = True