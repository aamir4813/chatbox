from application import app , db 
from flask import render_template , flash , redirect , url_for , request
from app_data.forms_wtf import *
from flask_login import login_user, current_user
from models.user_model import User

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    if current_user.is_authenticated :
        return redirect(url_for('chat'))

    # Update database if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash password
        password_hash = pbkdf2_sha256.hash(password)

        # Add username & hashed password to DB
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully. Please login.', 'success')
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)
