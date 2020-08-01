document.addEventListener('DOMContentLoaded', () => {

    var socket = io();
    let room = "Lounge";

    const username = document.querySelector('#get-username').innerHTML;

    // socket.on('connect', data => {
    //     console.log('HELLO');
    //     // socket.emit('some-event', { 'msg': 'this should work' });
    // });
    // socket.on('some-event-here', data => {
    //     console.log(data);
    // });
    document.querySelector('#send_message').onclick = () => {
        socket.emit('incoming-msg', {
            'msg': document.querySelector('#user_message').value,
            'username': username,
            'room': room
        });
        console.log('pressed \n');
        document.querySelector('#user_message').value = '';
    }


    socket.on('message', data => {

        if (data.msg) {
            const p = document.createElement('p');
            const span_username = document.createElement('span');
            const span_timestamp = document.createElement('span');
            const br = document.createElement('br')
            if (data.username == username) {
                p.setAttribute("class", "my-msg");

                span_username.setAttribute("class", "my-username");
                span_username.innerText = data.username;

                span_timestamp.setAttribute("class", "timestamp");
                span_timestamp.innerText = data.time_stamp;

                p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML

                document.querySelector('#display-message-section').append(p);
            } else if (typeof data.username !== 'undefined') {
                p.setAttribute("class", "others-msg");

                span_username.setAttribute("class", "other-username");
                span_username.innerText = data.username;

                span_timestamp.setAttribute("class", "timestamp");
                span_timestamp.innerText = data.time_stamp;

                p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;

                document.querySelector('#display-message-section').append(p);
            } else {
                printSysMsg(data.msg);
            }


        }
        scrollDownChatWindow();
    });

    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = () => {
            let newRoom = p.innerHTML
            if (newRoom === room) {
                msg = `You are already in ${room} room.`;
                printSysMsg(msg);
            } else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        };
    });

    document.querySelector("#logout-btn").onclick = () => {
        leaveRoom(room);
    };

    function leaveRoom(room) {
        socket.emit('leave', { 'username': username, 'room': room });

        document.querySelectorAll('.select-room').forEach(p => {
            p.style.color = "black";
        });
    }

    function joinRoom(room) {

        socket.emit('join', { 'username': username, 'room': room });

        document.querySelector('#' + CSS.escape(room)).style.color = "#ffc107";
        document.querySelector('#' + CSS.escape(room)).style.backgroundColor = "white";

        document.querySelector('#display-message-section').innerHTML = '';

        document.querySelector("#user_message").focus();
    }

    function scrollDownChatWindow() {
        const chatWindow = document.querySelector("#display-message-section");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function printSysMsg(msg) {
        const p = document.createElement('p');
        p.setAttribute("class", "system-msg");
        p.innerHTML = msg;
        document.querySelector('#display-message-section').append(p);
        scrollDownChatWindow()

        document.querySelector("#user_message").focus();
    }
});