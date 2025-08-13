from flask import Blueprint, session, redirect
from app.controllers.dashboard import dashboard_controller

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('login')
    return dashboard_controller()

@dashboard_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')