/* eslint-disable */
import { STORAGE_KEY } from './mutations'

export default function createSocketioPlugin(socket) {
    return store => {
        // socket.onclose = function() {}

        // socket.onmessage = function(e) {
        //     var data = JSON.parse(e.data);
        //     switch (data.command) {
        //         case 'get_token':
        //             store.commit('setToken', data.content);
        //             break; 
        //     }
        // }

        socket.on('chat', function(chat) {
            console.log(chat)
            store.commit('addMsg', chat);
        });

        socket.on('visitor list', function(list) {
            store.commit('setVisitorList', list)
        });

        socket.on('initMsg', function(messages) {
            console.log(messages)
            store.commit('initMsg', messages)
        });

         socket.on('get id', function(list) {
            store.commit('setId', list)
        });

        socket.on('visitor join', function(visitor) {
            store.commit('addVisitor', visitor)
        });

        store.subscribe(mutation => {
            switch (mutation.type) {
                case 'visitorJoin':
                    socket.emit('visitor join', mutation.payload)
                    break;
                case 'agentJoin':
                    socket.emit('agent join', mutation.payload);
                    break;
                case 'chat':
                console.log(mutation.payload)
                    socket.emit('chat', mutation.payload)
                    break;
                case 'joinUserRoom':
                    socket.emit('join user room', mutation.payload)
                    break;



                    // case 'sendMsg':
                    //     var ws_payload = {
                    //         command: "command",
                    //         content: mutation.payload
                    //     }
                    //     console.log('to socket server')
                    //     console.log(JSON.stringify(ws_payload))
                    //     ws.send(JSON.stringify(ws_payload))
                    //     break;
                    // case 'terminate':
                    //     var ws_payload = {
                    //         command: "terminate",
                    //         content: mutation.payload
                    //     }
                    //     console.log('to socket server')
                    //     console.log(JSON.stringify(ws_payload))
                    //     ws.send(JSON.stringify(ws_payload))
                    //     break;
            }
        })
    }
}
