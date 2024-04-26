import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mydatabase.db")
Session = sessionmaker(bind=engine)
session = Session()

# Create a table
Base = declarative_base()
class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create a row
person = Person(name='Alice', age=25)
session.add(person)
session.commit()

# Query the row
results = session.query(Person).filter_by(name='Alice').all()
print(results[0].age) # prints 25

# Update the row
person.age = 30
session.commit()

# Delete the row
session.delete(person)
session.commit()