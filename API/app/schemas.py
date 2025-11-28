from pydantic import BaseModel
from decimal import Decimal

class MetadataBase(BaseModel):
    LID: int
    GameID: str
    GameName: str
    LastModified: Decimal
    DeviceID: str
    Cloud: str

class MetadataCreate(MetadataBase):
    pass

class Metadata(MetadataBase):
    ID: int

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

class DownloadRequestBase(BaseModel):
    DeviceID: str
    Operation: str
    GameID: str
    Completed: bool
    TimeStamp: Decimal

class DownloadRequestCreate(DownloadRequestBase):
    pass 

class DownloadRequest(DownloadRequestBase):
    RequestID: int

    class Config: 
        orm_mode = True