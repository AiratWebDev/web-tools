from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Links(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    full_link = Column(String, index=True)
    short_link = Column(String, index=True, unique=True)

