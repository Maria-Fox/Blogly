"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
#set a  secret key for session cookies
app.config['SECRET_KEY'] = 'secret-key'
debug = DebugToolbarExtension(app)

# SQLAlch configs
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db connection & creation
connect_db(app)
db.create_all()

@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")

@app.route("/users")
def list_users():
  '''Show all users w/ links to view details page p/ user. Allow for new users to be created.'''

  users = User.query.all()
  return render_template ("index.html", users= users)


@app.route("/users/new")
def list_form():
  '''Show an add form for users'''

  return render_template ("createUser.html")

@app.route("/users/new", methods = ["POST"])
def create_user():
  '''Process the add form adding a new user and going back to /users'''

  first_name = request.form["first_name"]
  last_name = request.form["last_name"]
  image_url = request.form["image_url"]

  new_user = User(first_name = first_name, last_name = last_name, image_url = image_url)

  db.session.add(new_user)
  db.session.commit()

  return redirect(f"/users")

@app.route("/users/<int:user_id>")
def show_details(user_id):
  '''Show information about given user'''
  user = User.query.get_or_404(user_id)

  return render_template("details.html", user = user)

@app.route("/users/<int:user_id>/edit")
def edit_page(user_id):
  '''Show the edit page'''

  user = User.query.get_or_404(user_id)

  return render_template("editUser.html", user= user)

@app.route("/users/<int:user_id>/edit", methods= ["POST"])
def process_form(user_id):
  '''Process edit formreturning user to the /users page'''

  user = User.query.get_or_404(user_id)

# grab the user id and re-assign values to columns
  user.first_name = request.form['first_name']
  user.last_name = request.form['last_name']
  user.image_url = request.form['image_url']
  
  db.session.add(user)
  db.session.commit()
  return redirect("/users")

@app.route("/users/<int:user_id>/delete", methods = ["POST"])
def delete_user(user_id):
  '''Delete the user'''

  user = User.query.get_or_404(user_id)
  db.session.delete(user)
  db.session.commit()

  return redirect("/users")