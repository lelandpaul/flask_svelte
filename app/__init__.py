# coding: utf-8

from flask import Flask
from config import Config
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config.from_object(Config)
Markdown(app)

from app import routes
