from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class URL(Base):
    __tablename__ = 'urls'
    short_url = Column(String, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
