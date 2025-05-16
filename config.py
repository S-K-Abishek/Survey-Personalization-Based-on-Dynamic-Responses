import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///survey.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey.db'

db = SQLAlchemy(app)  # Initialize SQLAlchemy instance
