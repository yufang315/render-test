from sqlalchemy import Column, Integer, String, Text
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    author = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=True)
