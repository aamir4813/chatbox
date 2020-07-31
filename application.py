from flask import Flask
from flask_socketio import SocketIO

# Define Flask app
app = Flask(__name__)



#socketio config

socketio = SocketIO(app , manage_session=False)

@app.route('/')
def index():

    return "hello"


if __name__ == "__main__":
    socketio.run(app , debug=True)