from sqlalchemy import Column, DateTime, ForeignKey, func, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Transitions(Base):
    __tablename__ = "transitions"

    id = Column(Integer, primary_key=True)
    link_id = Column(ForeignKey("links.id"))
    link = relationship("Links")

    user = Column(String)