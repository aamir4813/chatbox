from flask_login import logout_user
from application import app , db 
from flask import render_template , flash , redirect , url_for , request
from app_data.forms_wtf import *

@app.route("/logout", methods=['GET'])
def logout():

    # Logout user
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))
