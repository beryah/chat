var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res) {
    res.sendfile('index.html');
});

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
        console.log('agent ' + agent.name + ' join user room id ' + agent.joinedId)
        socket.join(agent.joinedId)
        io.to(agent.joinedId).emit('agent joined', agent.name + ' joined your room, you can talk now');
    });

    socket.on('chat', function(chat) {
    	console.log(chat)
    	if(chat.roomId === undefined){
    		io.to(socket.id).emit('chat', chat);
    	}else{
    		io.to(chat.roomId).emit('chat', chat);
    	}        
    });

    // var joined = false;

    // socket.on('join', function(roomName) {
    //     if (joined) {
    //     	joined = true;
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
