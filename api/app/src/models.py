from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from src.init_database import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(UUID(as_uuid=True), primary_key=True)
    date_created = Column(TIMESTAMP, default=datetime.utcnow)
    user_ip = Column(String)
