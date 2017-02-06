/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import { state, mutations } from './mutations'
import plugins from './plugins'
import config from '../../config'
import io from 'socket.io-client';

// var ws = new WebSocket(process.env.WEBSOCKET);
var socket = io('localhost:3000');
Vue.use(Vuex)

// just return all state
export const getAllstate = state => state

const store = new Vuex.Store({
    state,
    mutations,
    plugins:[plugins(socket)]
})

export default store
