from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, String, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base


class Links(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, index=True, default=datetime.utcnow)
    full_link = Column(String(100))
    creator = Column(String(30))
    remove = Column(Boolean, default=False)

    transitions = relationship("Transitions")

    __mapper_args__ = {"eager_defaults": True}
