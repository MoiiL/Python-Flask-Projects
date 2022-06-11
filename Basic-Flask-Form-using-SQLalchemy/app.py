#modules required
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#flask instance
app = Flask(__name__)
#database creation
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///usersdatabase.db'      #sqlite is used here for quick demo
#secret key
app.config['SECRET_KEY'] = 'secret key'
#initializing the database 
db = SQLAlchemy(app)

#app model
class Users(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), nullable = False)
  email = db.Column(db.String(50), nullable = False, unique = True)
  password = db.Column(db.String(20), nullable = False)
  
  
#flask form
class UserForm(FlaskForm):
  username = StringField('Username', validators = [DataRequired()])
  email = StringField('Email', validators = [DataRequired()])
  password = StringField('Password', validators = [DataRequired()])
  submit = SubmitField('Submit')
  
  
 @app.route('/user/add', methods = ['GET', 'POST'])

def add_user():
   return render_templates('add_user.html')
  
  

  
  


  
 
  





