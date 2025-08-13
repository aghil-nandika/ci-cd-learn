from flask import request, redirect, render_template, session
from app.models.data import User
from app import db

def login_controller():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect('/')
        return render_template('login.html', error='username atau password salah...')

    return render_template('login.html')