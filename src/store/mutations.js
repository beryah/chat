/* eslint-disable */
function Session() {
    this.token = '';
    this.sessionId = '';
    this.status= 'idel';
    this.clientId= '';
    this.seq= '';
    this.version= '';
}

export const state = {
  supportId: 'michael_mao@trendmicro.com',
  sessions: [],
}

var firstSession = new Session();
firstSession.token = '2332232'
state.sessions.push(firstSession);

var s = new Session();
s.token = '23322sadads32'
state.sessions.push(s);

export const mutations = {
  set_token (state, payload, ) {
  	state.token = payload.token
    state.sessionId = payload.sessionId
  },
  get_token (state, payload) {
    var newSession = new Session();
    newSession.token = '123132'
    state.sessions.push(newSession);
  },
  sendMsg (state, payload){
  },
  getStatus (state, payload){
    
  },
  update_connect_status(state, status){
  	state.status = status
  },
}
