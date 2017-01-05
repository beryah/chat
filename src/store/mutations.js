/* eslint-disable */
import moment from 'moment'

function Session() {
    this.token = '000000';
    this.sessionId = '';
    this.connectedStatus = 'idel';
    this.clientId = '';
    this.supportId = 'michael_mao@trendmicro.com';
    this.seq = '';
    this.version = '';
    this.connectedStartTime = '';
    this.messages = [];
    this.commands = [];
}

export const state = {
    sessions: []
}

var firstSession = new Session();
state.sessions.push(firstSession);

export const mutations = {
    set_token(state, payload) {
        state.sessions[0].token = payload.token
        state.sessions[0].sessionId = payload.sessionId
        state.sessions[0].connectedStatus = 'Waiting for Client Connect'        
    },
    get_token(state, payload) {
        state.sessions[0].connectedStatus = 'Registing token id'
    },
    sendMsg(state, payload) {
        var message = new Message()
        message.timestamp = ''
        message.content = payload.content.content.wording
        state.sessions[0].messages.push(message)
        state.sessions[0].commands.push(payload)

        var m = new Message()
        m.timestamp = ''
        m.content = 'Hello, I am Michael and I need help. Could you help me cdoing'
        m.fromClient = true
        state.sessions[0].messages.push(m)
    },
    getStatus(state, payload) {
        if ('initArg' in payload) {
            state.sessions[0].connectedStatus = 'Connected'
            state.sessions[0].version = payload.initArg.version
            state.sessions[0].connectedStartTime = moment().format('YYYY-MM-DD hh:mm:ss')
        }

        if ('cmdStatus' in payload) {
            for (var prop in payload.cmdStatus) {
                var obj = payload.cmdStatus[prop].content
                if (obj.hasOwnProperty('wording')) {
                    var message = new Message()
                    message.timestamp = payload.cmdStatus[prop].created
                    message.content = obj.wording
                    state.sessions[0].messages.push(message)
                }
            }
        }
    },
    update_connect_status(state, status) {
        state.status = status
    },
}

function Message() {
    this.timestamp = '';
    this.content = '';
    this.fromClient = false;
}
