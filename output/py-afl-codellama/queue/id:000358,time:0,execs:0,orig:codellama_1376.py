import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for our database models
Base = declarative_base()

# Create a table to store user data
class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    email = sqlalchemy.Column(sqlalchemy.String(255), unique=True)

# Create a sessionmaker to interact with the database
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test that an email address is valid
def test_email(email):
    assert email, "Email address must be provided"
    if not sqlalchemy.inspect(email).valid:
        raise ValueError("Invalid email address")

# Test that a user's name is valid
def test_name(name):
    assert name, "Name must be provided"
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long")

# Add a new user to the database
def add_user(email, name):
    test_email(email)
    test_name(name)
    session.add(User(email=email, name=name))
    session.commit()