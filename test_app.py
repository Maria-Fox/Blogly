from flask import Flask, pytest
from app import app
from unittest import TestCase
from models import User

class UsersTestCase(TestCase):
  '''Testing the user routes within app.py'''

def setUp(self):
  '''Initiate before every test'''

  self.client = app.test_client()
  app.config['Testing'] = True

def test_list_users(self):
  '''Test root firector status & response'''

  response = self.client.get("/home")
  html = response.get_data(as_text=True)

  self.assertEqual(response.status_code,200)
  self.assertIn('<h2 id="list-header">Users</h2>', response.data)


def test_list_form(self):
  '''Test ability to route into creating a new user page.'''

  response = self.client.get("/users/new")
  html = response.get_data(as_text = True)

  self.assertEqual(response.status_code,200)
  self.asserIn("<button type='submit'>Create User</button>", response.data)

def test_create_user(self):
  '''Test ability to add new user to DB'''

  response = self.client.post('/users/new', follow_redirects= True,data = {'first_name' : 'Test1', 'last_name': 'test2'})

  html = response.get_data(as_text = True)

  self.assertEqual(response.status_code, 200)
  self.assertIn("<ul id='user-list'>", response.data)


def test_edit_page(self):
  '''Test web ability to grab DB person based on id'''

  response = self.client.get("/users/<int:2>/edit")
  html = response.get_data(as_text = True)

  self.assertEqual(response.status_code, 200)
  self.assertIn("<h1 id='header'>Edit User Profile</h1>", response.data)

  


