from pydantic import BaseModel
from decimal import Decimal

class LocalMetadataBase(BaseModel):
    GameID: str
    GameName: str
    LastModified: Decimal
    DeviceID: str

class LocalMetadataCreate(LocalMetadataBase):
    pass

class LocalMetadata(LocalMetadataBase):
    GameID: str

    class Config:
        orm_mode = True

class UploadRequestBase(BaseModel):
    DeviceID: str
    Operation: str
    GameID: str
    Completed: bool
    TimeStamp: Decimal

class UploadRequestCreate(UploadRequestBase):
    pass 

class UploadRequest(UploadRequestBase):
    RequestID: int

    class Config: 
        orm_mode = True