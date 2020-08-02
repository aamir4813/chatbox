import os
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from models.user_model import *
from app_data.forms_wtf import *
from flask_login import LoginManager

# Define Flask app
app = Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")

load_dotenv()

# DB config
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("SQLALCHEMY_STATUS")
db = SQLAlchemy(app)

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

# import sockets
from app_data.sockets import *


if __name__ == "__main__":
    app.run()