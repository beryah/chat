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
      if (data.content == 'test success'){
        store.commit('update_connect_status', 'connected');        
      }else{
        
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