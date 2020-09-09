from typing import Optional

from pydantic import BaseModel

from uuid import UUID
from datetime import datetime


# Shared properties
class ContentsignagesBase(BaseModel):
    content_id: UUID
    signage_id: UUID
    signage_tmstp: datetime


# Properties to receive on Contentsignages creation
class ContentsignagesCreate(ContentsignagesBase):
    name: str


# # Properties to receive on Contentsignages update
# class ContentsignagesUpdate(ContentsignagesBase):
#     pass


# Properties shared by models stored in DB
class ContentsignagesInDBBase(ContentsignagesBase):
    content_id: UUID
    signage_id: UUID
    signage_tmstp: datetime


    class Config:
        orm_mode = True


# # Properties to return to client
# class Contentsignages(ContentsignagesInDBBase):
    


# # Properties properties stored in DB
# class ContentsignagesInDB(ContentsignagesInDBBase):
#     pass
