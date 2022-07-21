"""Models for Blogly."""
from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
db = SQLAlchemy()
import datetime

standard_pic_URL = "https://images.unsplash.com/photo-1549633030-89d0743bad01?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Z29vZCUyMGx1Y2t8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60"

def connect_db(app):
  '''Connect to database.'''
  
  db.app = app
  db.init_app(app)

class User(db.Model):
  # must pass in subclass of db.model

  def __repr__(self):
    '''Show info about user'''
    u = self
    return f"<User {u.user_id} {u.first_name} {u.last_name} {u.image_url}>"

  __tablename__ = "users"
  
  user_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
  first_name = db.Column(db.Text, nullable = False)
  last_name = db.Column(db.Text)
  image_url = db.Column(db.Text, default=standard_pic_URL)

  # conncts to Post class, dletes all users posts by cascading if user is deleted
  posts = db.relationship('Post', cascade = "all, delete-orphan")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Post(db.Model):
  '''Posts'''

  def __repr__(self):
    '''Show info about posts'''

    p = self
    return f"<Post includes {p.id}, {p.title}, {p.content}, {p.created_at}, from {p.user_id}>"

  __tablename__ = "posts"

  post_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
  title = db.Column(db.Text, nullable = False)
  content = db.Column(db.Text, nullable = False)
  created_at = created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)

# connects to User class
  users = db.relationship('User')


