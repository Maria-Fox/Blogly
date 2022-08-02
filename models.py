"""Models for Blogly."""
from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
db = SQLAlchemy()
import datetime

standard_pic_URL = "https://images.unsplash.com/photo-1600265360004-c16515250359?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDR8fGZyaWVuZHN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"

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
  image_url = db.Column(db.Text, default = standard_pic_URL)

  # conncts to Post class, deletes all users posts by cascading if user is deleted
  posts = db.relationship('Post', backref = "user", cascade = "all, delete-orphan")

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

# Relationships 
  users = db.relationship('User')
  ptag_1 = db.relationship('PostTag')
  thru_rel = db.relationship('Tag', secondary  = 'post_tags')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Tag(db.Model):
    '''Holds tag and post id.'''

    def __repr__(self):
      '''Include post id and post creator.'''

      t = self
      return f"<The tag name is {t.name} with an id of {t.id}>"

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.Text, nullable = False, unique = True)

    # ptag_2 = db.relationship('PostTag')
    # thru_rel = db.relationship('Post', secondary  = 'post_tags')
    posts = db.relationship(
        'Post',
        secondary="post_tags",
        # cascade="all,delete",
        backref="tags",
    )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


class PostTag(db.Model):
    '''Holds posttag id and tag id'''

    def __repr__(self):

      p = self

      return f"This post id : {p.post__id} with a tag id of {p.tag_id}"

    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key = True)

    # post_rel = db.relationship('Post')
    # tag_rel = db.relationship('Tag')







    


