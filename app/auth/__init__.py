from flask import Blueprint
from app import auth

bp = Blueprint('auth', __name__)

from app.auth import email, forms, routes

