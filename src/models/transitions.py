from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime


from .base import Base


class Transitions(Base):
    __tablename__ = "transitions"

    id = Column(Integer, primary_key=True)
    link_id = Column(ForeignKey("links.id", ondelete="CASCADE"), nullable=False)
    link = relationship("Links")
    created_at = Column(DateTime, index=True, default=datetime.utcnow)


    user = Column(String)