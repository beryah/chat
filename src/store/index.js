/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import { state, mutations } from './mutations'

Vue.use(Vuex)

// just return all state
export const getAllstate = state => state

const store = new Vuex.Store({
  state,
  mutations
})

export default store