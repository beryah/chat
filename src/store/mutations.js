/* eslint-disable */
import moment from 'moment'

function Session() {
    this.token = '000000';
    this.sessionId = '';
    this.connectedStatus = 'idel';
    this.clientId = 'user@trend.account.email';
    this.supportId = 'michael_mao@trendmicro.com';
    this.seq = '';
    this.version = '';
    this.source = 'DLS'
    this.connectedStartTime = '';
    this.messages = [];
    this.commands = {};
    this.currentCommandSeq = 0;
}

function Message() {
    this.fromMe = true
    this.word = ''
}

export const state = {
    sessions: [],
    qcases: [],
    showStarter: true,
    visitorName: '',
    showVisitorInfo: true,
    messages: [],
    visitors: [],
    visitorsMessage: {},
    agentName: '',
    showAgentChatRoom: false,
    joinedRoomId: '',
    visitorSocketId: '',
    openSound: true
}

var firstSession = new Session();
state.sessions.push(firstSession);

export const mutations = {
    getToken(state, payload) {
        state.sessions[0].connectedStatus = 'Registing token id'
    },
    setToken(state, payload) {
        state.sessions[0].token = payload.token
        state.sessions[0].sessionId = payload.sessionId
        state.sessions[0].connectedStatus = 'Waiting for Client Connect'
    },
    setTerminate(state, payload) {
        if (payload.status == "OK") {
            state.sessions[0].connectedStatus = 'Disconnected'
        } else {
            alert('terminate fail')
            console.log(payload)
        }
    },
    agentJoin(state, payload) {
        state.agentName = payload
    },
    joinUserRoom(state, payload) {
        console.log(payload)
        state.joinedRoomId = payload.joinedRoomId
        state.showAgentChatRoom = true
        state.visitorSocketId = payload.joinedRoomId
    },
    terminate(state, payload) {},
    switchStarter(state, payload) {
        state.showStarter = payload
    },
    switchVisitorInfo(state, payload) {
        state.showVisitorInfo = payload
    },
    visitorJoin(state, payload) {
        state.visitorName = payload
    },
    setVisitorList(state, payload) {
        state.visitors = payload
    },
    initMsg(state, payload) {
        state.messages = payload.messages;
        console.log('----' + payload.id)
        state.visitorsMessage[payload.id] = payload.messages;
    },
    addVisitor(state, payload) {
        state.visitors.push(payload)
    },
    setId(state, payload) {
        state.visitorSocketId = payload.id
    },
    chat(state, payload) {},
    addMsg(state, payload) {
        console.log(payload)
        state.messages.push(payload)
        console.log(state.visitorsMessage)
        console.log(state.joinedRoomId)
        console.log(state.visitorsMessage[state.joinedRoomId])
        state.visitorsMessage[state.joinedRoomId].push(payload) 

        // if (state.openSound) {
        //     new Audio("/static/briefcase-lock.mp3").play();;
        // }
    },
    sendMsg(state, payload) {
        var message = new Message()
        var now = new Date()
        message.timestamp = now
        message.formatedTime = moment(now).format('YYYY/MM/DD hh:mm')
        message.content = payload.content.content.wording
        message.arrived = false
        message.seq = payload.seq
        state.sessions[0].messages.push(message)
        state.sessions[0].commands[payload.seq] = payload
        state.sessions[0].commands[payload.seq].status = false
        state.sessions[0].currentCommandSeq++

            //test code, can get client message without server
            // var m = new Message()
            // m.timestamp = ''
            // m.content = 'Hello, I am Michael and I need help. Could you help me cdoing'
            // m.fromClient = true
            // state.sessions[0].messages.push(m)
    },
    getStatus(state, payload) {
        //client grab token 
        if ('initArg' in payload) {
            state.sessions[0].connectedStatus = 'Connected'
            state.sessions[0].version = payload.initArg.version
            state.sessions[0].connectedStartTime = moment().format('YYYY-MM-DD hh:mm:ss')
        }

        if ('cmdStatus' in payload) {
            for (var prop in payload.cmdStatus) {
                var content = payload.cmdStatus[prop].content
                if (content.hasOwnProperty('wording')) {
                    var message = new Message()
                    message.timestamp = payload.cmdStatus[prop].created
                    message.content = content.wording
                    message.fromClient = true
                    message.formatedTime = moment(message.timestamp * 1000).format('YYYY/MM/DD hh:mm')
                    message.seq = prop
                    state.sessions[0].messages.push(message)
                }

                if (content.hasOwnProperty('asSeqStatus')) {
                    if (content.asSeqStatus == 'OK' && prop < 1000) {
                        for (var i = 0; i < state.sessions[0].messages.length; i++) {
                            if (state.sessions[0].messages[i].seq == prop) {
                                state.sessions[0].messages[i].arrived = true
                            }
                        }
                        state.sessions[0].commands[prop].status = true
                    }
                }
            }
        }
    },
    setNewCase(state, payload) {
        state.qcases.push(payload.tuka[0])
    },
    update_connect_status(state, status) {
        state.status = status
    },
}
