import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    address = Column(String(250), nullable=True)
    phone_number = Column(String(30), nullable=False)
    creation_date = Column(String(30), nullable=False)


class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table follower
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_from = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to = relationship(User)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table post
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class MediaType(enum.Enum):
    album = 1
    photo = 2
    story = 3
    video = 4

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table media
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mediatype = Column(Enum(MediaType))
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table comment
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)







# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e