/* eslint-disable */
export const state = {
  token : '',
  status: 'idel',
  clientId: '',
  sessionId: '',
  supportId: 'michael_mao@trendmicro.com',
  seq: 0,
  version: ''
}

export const mutations = {
  set_token (state, payload, ) {
  	state.token = payload.token
    state.sessionId = payload.sessionId

  },
  get_token (state, payload) {
    //this.$store.commit('update_connect_status', 'wait for connect')
  },
  sendMsg (state, payload){
  },
  getStatus (state, payload){
    
  },
  update_connect_status(state, status){
  	state.status = status
  },
}
