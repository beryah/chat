var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var redis = require('redis');

// var sub = redis.createClient(3158, '50.30.35.9', { auth_pass: '95bb24a07fe7a97d7958bba081faf508' });
// var pub = redis.createClient(3158, '50.30.35.9', { auth_pass: '95bb24a07fe7a97d7958bba081faf508' });

var sub = redis.createClient(6379, '10.1.180.22');
var pub = redis.createClient(6379, '10.1.180.22');


sub.subscribe('chat');

app.get('/admin', function(req, res) {
    res.sendfile('admin.html');
});

app.use(express.static('public'));

var users = {}
var agents = {}

io.on('connection', function(socket) {
    console.log('someone connected:' + socket.id);

    socket.on('visitor join', function(name) {
        console.log('visitor join ' + name)
        users[name] = { name: name, id: socket.id };
        io.emit('visitor join', { name: name, id: socket.id })
    });

    socket.on('agent join', function(name) {
        console.log('agent join ' + name)
        agents[name] = { name: name, id: socket.id };
        socket.emit('user list', users)
    });

    socket.on('join user room', function(agent) {
        console.log(agent.name + ' joined ' + agent.joinedId)
        socket.join(agent.joinedId)
        io.to(agent.joinedId).emit('chat', { msg: agent.name + ' joined', from: 'system' });
    });

    socket.on('chat', function(chat) {
        console.log(chat)
        pub.publish('chat', JSON.stringify(chat));
    });

    sub.on('message', function(channel, chat) {
        chat = JSON.parse(chat)
        if (chat.roomId === undefined) {
            io.to(socket.id).emit('chat', chat);
        } else {
            io.to(chat.roomId).emit('chat', chat);
        }
    });

    // var joined = false;

    // socket.on('join', function(roomName) {
    //     if (joined) {
    //      joined = true;
    //         return;
    //     }
    //     console.log(roomName)
    //     socket.join(roomName)
    //     socket.broadcast.to(roomName).emit('romm msg', 'broadcast to ' + roomName);
    //     io.to(roomName).emit('room msg', 'io emmit' + roomName);
    // });
    //io.to(id).emit('id', socket.id);
    //io.emit('some event', { for: 'everyone' }); every one
    //socket.broadcast.emit('hi');
});

http.listen(3000, function() {
    console.log('listening on *:3000');
});
