/* eslint-disable */
export const state = {
  token : '',
  status: 'idel',
  clientId: ''
}

export const mutations = {
  set_token (state, token) {
  	state.token = token
  },
  get_token (state, a) {
    
  },
  update_connect_status(state, status){
  	state.status = status
  },
}
