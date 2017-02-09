var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var redis = require('redis');

 var sub = redis.createClient(6379, '127.0.0.1');
 var pub = redis.createClient(6379, '127.0.0.1');

//test redis pub.on('connect', () => console.log('Connected to Redis') )

sub.subscribe('chat');

app.get('/admin', function(req, res) {
    res.sendfile('admin.html');
});

app.use(express.static('public'));

var visitors = []
var agents = {}

io.on('connection', function(socket) {
    console.log('someone connected:' + socket.id);

    socket.on('visitor join', function(name) {
        console.log('visitor join ' + name)
        visitors.push({ name: name, id: socket.id });
        io.emit('visitor join', { name: name, id: socket.id })
    });

    socket.on('agent join', function(name) {
        console.log('agent join ' + name)
        agents[name] = { name: name, id: socket.id };
        socket.emit('visitor list', visitors)
    });

    socket.on('join user room', function(agent) {
        console.log(agent.name + ' joined ' + agent.joinedRoomId)
        socket.join(agent.joinedRoomId)
        io.to(agent.joinedRoomId).emit('chat', { msg: agent.name + ' joined', from: 'system' });
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
