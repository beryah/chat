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
          store.commit('set_token', data);
        case 'getStatus' :          
          store.commit('getStatus', data);
      }
    } 

    store.subscribe(mutation => {
      switch (mutation.type){
        case 'get_token':
          ws.send(JSON.stringify(mutation.payload))
        case 'sendMsg':
          ws.send(JSON.stringify(mutation.payload))
      }      
    })
  }
}