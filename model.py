from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)

    profile = relationship("Profile", back_populates="user", uselist=False)
    posts = relationship("Post", back_populates="author")

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="profile")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    posts = relationship("Post", secondary=post_tags, back_populates="tags")
