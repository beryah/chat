/* eslint-disable */
import { STORAGE_KEY } from './mutations'

export default function createWebSocketPlugin (ws) {
  return store => {
    ws.onopen = function() {
      console.log("Connected!");  
    }

    ws.onclose = function() {
      store.commit('update_connect_status', 'ws close');        
    }

    ws.onmessage = function(e) {
      console.log(e.data)
      var data = JSON.parse(e.data);
      switch(data.tsew_command){
        case 'get_token':
          console.log(data.clientId)
          store.commit('update_connect_status', 'connected');
          store.commit('set_token', data.token, data.clientId);
      }
    } 

    store.subscribe(mutation => {
      if (mutation.type === 'get_token') {
        var get_token = {
          tsew_command: 'get_token',
          content: mutation.payload
        }        
        ws.send(JSON.stringify(get_token))
      }
    })
  }
}