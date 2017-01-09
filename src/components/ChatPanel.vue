<template>
    <div>
        <ul class="nav nav-tabs" role="tablist">
            <li v-for="(session, index) in sessions" role="presentation" v-bind:class="{active: index == 0}">
                <a :href="'#a' +session.token" :aria-controls="'a'+session.token" role="tab" data-toggle="tab">
                    {{session.token}}
                </a>
            </li>
        </ul>
        <div class="tab-content">
            <div v-for="(session, index) in sessions" v-bind:class="{'tab-pane': true, active: index == 0}" :id="'a'+session.token" role="tabpanel">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <SessionManager />
                        <SessionStatus :session="session" />
                    </div>
                    <ChatPanelBody :messages="session.messages" />
                    <div class="panel-footer pf">
                        <button class="btn btn-success" type="button" @click='capture'>
                            <span class="glyphicon glyphicon-camera" aria-hidden="true"></span> Capture
                        </button>
                    </div>
                    <div class="panel-footer pf">
                        <textarea @keyup.enter="sendMsg($event)" class="form-control" rows="5" placeholder="Write you message here..." v-model="msg" />
                        <!-- /input-group -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
.panel-body {
    height: 200px;
}

.pf {
    width: 60%;
}
</style>
<script>
import SessionManager from './SessionManager.vue'
import SessionStatus from './SessionStatus.vue'
import ChatPanelBody from './ChatPanelBody.vue'

export default {
    data() {
            return {
                msg: ''
            }
        },
        components: {
            SessionManager,
            SessionStatus,
            ChatPanelBody
        },
        methods: {
            sendMsg(e) {
                if (e.shiftKey) {
                    return;
                }
                var payload = {
                    clientId: this.$store.state.sessions[0].clientId,
                    supportId: this.$store.state.sessions[0].supportId,
                    token: this.$store.state.sessions[0].token,
                    sessionId: this.$store.state.sessions[0].sessionId,
                    seq: this.$store.state.sessions[0].currentCommandSeq,
                    content: {
                        msgId: "50397190",
                        content: {
                            wording: this.msg,
                            confirmation: "",
                        }
                    }
                }
                this.$store.commit('sendMsg', payload)
                this.msg = ''
            },
            capture() {},
        },
        computed: {
            sessions() {
                return this.$store.state.sessions;
            },
            getTabCss(index) {
                if (index == 0)
                    return "active";
                else
                    return "";
            }

        }
}
</script>
