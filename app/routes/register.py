from flask import Blueprint
from app.controllers.register import register_controller

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    return register_controller()