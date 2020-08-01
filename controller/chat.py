from application import app
from flask import flash , render_template , redirect , url_for 
from flask_login import current_user

ROOMS = ["Launge" , "Gaming" , "Coding"  ]
@app.route("/chat", methods=['GET', 'POST'])
def chat():

    if not current_user.is_authenticated:
        flash('Please login', 'danger')
        return redirect(url_for('login'))

    return render_template("chat.html", username=current_user.username, rooms=ROOMS)
