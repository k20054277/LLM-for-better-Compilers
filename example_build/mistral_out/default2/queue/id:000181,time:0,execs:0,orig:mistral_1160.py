
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.ext.declarative import declarative_base

# Set up database connection
Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()
Session = sessionmaker(bind=engine)

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<Person {self.name}>"

Base.metadata.create_all(engine)
