
from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define Base class for SQLAlchemy ORM
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)

# Create engine to connect to database
engine = create_engine('sqlite:///test.db', echo=False)

# Create table in the database if it doesn't exist
Base.metadata.create_all(engine)

# Define a session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user to the database
new_user = User(id=1, is_active=True)
session.add(new_user)
session.commit()

# Update an existing user's status in the database
existing_user = session.query(User).filter_by(id=1).first()
if existing_user:
    existing_user.is_active = False
    session.commit()
else:
    print("User with id 1 not found")

# Fetch users from the database and check their statuses
users = session.query(User).all()
for user in users:
    print(f"User {user.id} is active: {user.is_active}")
