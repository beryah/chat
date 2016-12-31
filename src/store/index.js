/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import { state, mutations } from './mutations'
import plugins from './plugins'

var ws = new WebSocket('ws://localhost:9010');

Vue.use(Vuex)

// just return all state
export const getAllstate = state => state

const store = new Vuex.Store({
  state,
  mutations,
  plugins:[plugins(ws)]
})

export default store