from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base

import uuid



class Signages(Base):
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4, unique=True, index=True)
    rec_time = create_at = Column(DateTime)
    content_id = Column(String) #TODO : update UUID, foreigkey
    face_id = Column(String)
    action_id = Column(String)
    viewaction_id = Column(String)
    viewpoint_id = Column(String)
    gender_id = Column(String)
    generation_id = Column(String)
    create_at = Column(DateTime)
    create_usr = Column(String)
    update_at = Column(DateTime)
    update_usr = Column(String)

