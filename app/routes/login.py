from flask import Blueprint
from app.controllers.login import login_controller

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    return login_controller()