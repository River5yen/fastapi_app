from typing import Optional

from pydantic import BaseModel

from uuid import UUID


# Shared properties
class ContentsBase(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    status: Optional[int] = 1


# Properties to receive on Contents creation
class ContentsCreate(ContentsBase):
    name: str


# # Properties to receive on Contents update
# class ContentsUpdate(ContentsBase):
#     pass


# Properties shared by models stored in DB
class ContentsInDBBase(ContentsBase):
    id: UUID
    name: str
    status: int


    class Config:
        orm_mode = True


# # Properties to return to client
# class Contents(ContentsInDBBase):
#     status: str


# # Properties properties stored in DB
# class ContentsInDB(ContentsInDBBase):
#     pass
