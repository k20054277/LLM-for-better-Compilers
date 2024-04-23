
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, and_, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    posts = relationship("Post", backref="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User")

def main():
    engine = create_engine('sqlite:///test.db', echo=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create operation
    new_user = User(name='John Doe', age=30)
    session.add(new_user)
    session.commit()

    print("New user created:")
    print(session.query(User).filter(User.id == new_user.id).first())

    # Read operation
    users = session.query(User).order_by(desc(User.age)).limit(2).all()
    for user in users:
        print(f"{user.name} ({user.age}): {[p.title for p in user.posts]}")

    # Update operation
    user = session.query(User).filter(User.name == 'John Doe').first()
    if user:
        user.age += 1
        session.commit()

    # Delete operation
    post = session.query(Post).filter(Post.title == "Old Post").first()
    if post:
        author = post.author
        session.delete(post)
        session.commit()
        print(f"Deleted post with title '{post.title}'")

if __name__ == '__main__':
    main()
