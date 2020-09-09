from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base

import uuid



class Contents(Base):
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4, unique=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    image = Column(String)
    status = Column(Integer)
    create_at = Column(DateTime)
    create_usr = Column(String)
    update_at = Column(DateTime)
    update_usr = Column(String)
