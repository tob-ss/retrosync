from pydantic import BaseModel
from decimal import Decimal

class MetadataBase(BaseModel):
    LID: str
    GameID: str
    GameName: str
    LastModified: Decimal
    DeviceID: str
    Cloud: str

class MetadataCreate(MetadataBase):
    pass

class Metadata(BaseModel):
    ID: int
    DeviceID: str

    class Config:
        orm_mode = True

class Metadata_Device(MetadataBase):
    DeviceID: str

class SyncRequestsBase(BaseModel):
    DeviceID: str
    Operation: str
    GameID: str
    Completed: bool
    TimeStamp: Decimal

class SyncRequestsCreate(SyncRequestsBase):
    pass 

class SyncRequests(SyncRequestsBase):
    RequestID: int

    class Config: 
        orm_mode = True