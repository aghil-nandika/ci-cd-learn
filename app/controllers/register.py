from flask import render_template, request, redirect, session
from app import db
from app.models.data import User

def register_controller():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        exist_user = User.query.filter_by(username=username).first()
        if exist_user:
            return render_template('register.html', error='username sudah digunakan')
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    return render_template('register.html')