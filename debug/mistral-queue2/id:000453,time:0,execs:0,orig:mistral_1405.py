
from sqlalchemy import create_engine, Column, Integer, String, Float, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import assertpy as assertp

# Set up database connection
engine = create_engine('sqlite:///testdb.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Create User table if not exists
Base.metadata.create_all(engine)

def insert_user(session, user):
    session.add(User(name=user['name']))
    session.commit()

def get_users(session):
    return session.query(User.id, User.name).all()

# Set up test data and validation using assertpy
test_data = [
    {'name': 'John Doe'},
    {'name': ''},
    {'name': None}
]

def test_insert_user():
    session = Session()

    for user in test_data:
        insert_user(session, user)
        assertp.is_instance(session.query(User.id).filter_by(name=user['name']).first(), User)
        assertp.that(session.query(User.name).filter_by(name=user['name']).first().name).is_equal_to(user['name'])
        session.close()

test_insert_user()
