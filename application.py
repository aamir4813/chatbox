from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from models.user_model import *
from app_data.forms_wtf import *
from flask_login import LoginManager
# Define Flask app
app = Flask(__name__)
app.secret_key="heythisisme"


# DB config
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']="postgres://ipzvyjpoapobve:9ddb079044385255fe35a7cf31fce27476c92360104cd14c1cb9ac05332181ff@ec2-3-216-129-140.compute-1.amazonaws.com:5432/d8oth2s9b514qc"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configure Flask Login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


#socketio config
socketio = SocketIO(app , manage_session=False)


# import every controller here
from controller.index import *
from controller.login import *
from controller.logout import *
from controller.chat import *

if __name__ == "__main__":
    socketio.run(app , debug=True)