# views/user.py
from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/user')
def user_home():
    return 'User Home Page'
