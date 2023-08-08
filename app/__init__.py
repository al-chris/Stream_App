import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_socketio import SocketIO, emit
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


app=Flask(__name__)
app.secret_key= os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import models
from app import views
