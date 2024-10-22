from application import app , db 
from flask import render_template , flash , redirect , url_for , request
from app_data.forms_wtf import *
from flask_login import current_user , login_user


@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated :
        return redirect(url_for('chat'))


    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        db.session.remove()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)
