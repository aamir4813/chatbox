from application import socketio

from flask_socketio import leave_room , join_room , send , emit 
from time import localtime , strftime

import eventlet
eventlet.monkey_patch()


@socketio.on('incoming-msg')
def on_message(data):

    print(f'\n\n{data}\n\n')
    msg = data["msg"]
    username = data["username"]
    room = data["room"]
    time_stamp = strftime('%b-%d %I:%M%p', localtime())
    send({"username": username, "msg": msg, "time_stamp": time_stamp}, room=room)


@socketio.on('join')
def on_join(data):
    """User joins a room"""

    username = data["username"]
    room = data["room"]
    join_room(room)

    send({"msg": username + " has joined the " + room + " room."}, room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room"""

    username = data['username']
    room = data['room']
    leave_room(room)
    send({"msg": username + " has left the room"}, room=room)


# @socketio.on('some-event')
# def do_here(data):
#     print(f'\n\n yes we got that \n\n')
#     send(data)
#     emit( 'some-event-here' , {'msg':'This is custome message'})