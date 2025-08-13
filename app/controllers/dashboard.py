from flask import request, render_template, redirect, session
from app.models.data import Note, Product
from app import db

def dashboard_controller():
    if request.method == 'POST':
        submit_type = request.form.get('submit_type')

        if submit_type == 'note':
            title = request.form.get('title')
            content = request.form.get('content')
            new_note = Note(title=title, content=content, user_id=session['user_id'])
            db.session.add(new_note)

        elif submit_type == 'product':
            name = request.form.get('name')
            description = request.form.get('description')
            new_product = Product(name=name, description=description, user_id=session['user_id'])
            db.session.add(new_product)

        db.session.commit()
        return redirect('/')

    notes = Note.query.filter_by(user_id=session['user_id']).all()
    products = Product.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', notes=notes, products=products)