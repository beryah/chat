/* eslint-disable */
import { STORAGE_KEY } from './mutations'

export default function createWebSocketPlugin(ws) {
    return store => {
        ws.onopen = function() {
            console.log("Connected!");
        }

        ws.onclose = function() {}

        ws.onmessage = function(e) {
            console.log('from socket server')
            console.log(e.data)
            var data = JSON.parse(e.data);
            switch (data.command) {
                case 'get_token':
                    store.commit('set_token', data.content);
                    break;
                case 'getStatus':
                    store.commit('getStatus', data.content);
                    break;
            }
        }

        store.subscribe(mutation => {            
            switch (mutation.type) {
                case 'get_token':
                    var ws_payload = {
                        command: "get_token",
                        content: mutation.payload
                    }                
                    console.log('to socket server')    
                    console.log(JSON.stringify(ws_payload))
                    ws.send(JSON.stringify(ws_payload))
                    break;
                case 'sendMsg':                  
                    var ws_payload = {
                        command: "command",
                        content: mutation.payload
                    }
                    console.log('to socket server')
                    console.log(JSON.stringify(ws_payload))
                    ws.send(JSON.stringify(ws_payload))
                    break;
            }
        })
    }
}
