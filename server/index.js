var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var config = require('config');
var redis = require('redis');
var redisConfig = config.get('Redis');
var redisClient = redis.createClient(redisConfig.port, redisConfig.host);
var pub = redis.createClient(redisConfig.port, redisConfig.host);

//test redis pub.on('connect', () => console.log('Connected to Redis') )

app.use(express.static('public'));

var visitors = []
var agents = {}

io.on('connection', function(socket) {
    var sub = redis.createClient(redisConfig.port, redisConfig.host);
    sub.subscribe(socket.id)

    socket.on('visitor join', function(name) {
        visitors.push({ name: name, id: socket.id });
        socket.emit('get id', { name: name, id: socket.id })
        io.emit('visitor join', { name: name, id: socket.id })
    });

    socket.on('agent join', function(name) {
        agents[name] = { name: name, id: socket.id };
        socket.emit('visitor list', visitors)
    });

    socket.on('join user room', function(agent) {
        sub.subscribe(agent.joinedRoomId)
        var id = agent.joinedRoomId
        socket.join(id)
        msg = { msg: agent.name + ' joined', from: 'system' }
        
        redisClient.lrange(id, 0, -1, function(err, reply) {
            socket.emit('initMsg', { id: id, messages: JSON.parse('[' + reply + ']') })
        });

        redisClient.lrange(id + "-joined", 0, -1, function(err, joinedAgentList) {
            if (joinedAgentList.indexOf(socket.id) == -1) {
                redisClient.rpush([id, JSON.stringify(msg)])
                redisClient.rpush([id + "-joined", socket.id])
                io.to(agent.joinedRoomId).emit('chat', msg);
            }


        });
    });

    socket.on('chat', function(chat) {
        redisClient.rpush(chat.roomId, JSON.stringify(chat))
        pub.publish(chat.roomId, JSON.stringify(chat));
    });

    sub.on('message', function(channel, chat) {
        chat = JSON.parse(chat)
        if (chat.roomId == channel) {
            console.log(chat)
            socket.emit('chat', chat);
        }
    });
});

http.listen(3000, function() {
    console.log('listening on *:3000');
});
