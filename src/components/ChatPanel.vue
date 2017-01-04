<template>
    <div>
        <ul class="nav nav-tabs" role="tablist">
            <li v-for="(session, index) in sessions" role="presentation">
                <a :href="'#a' +session.token" :aria-controls="'a'+session.token" role="tab" data-toggle="tab" v-bind:class="{active: index == 0}">
    				{{session.token}}
    			</a>
            </li>
        </ul>
        <div class="tab-content">
            <div v-for="(session, index) in sessions" v-bind:class="{'tab-pane': true, active: index == 0}" :id="'a'+session.token" role="tabpanel">
                <div class="panel-heading">
                    <SessionManager />
                    <SessionStatus :session="session" />                    
                </div>
                <div class="panel panel-default">
                    <div class="panel-body">
                    </div>
                    <div class="panel-footer">
                        <div class="input-group">
                            <input type="text" class="form-control">
                            <span class="input-group-btn">
			        <button class="btn btn-success" type="button" @click='sendMsg'>Send</button>
			      </span>
                        </div>
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
</style>
<script>
import SessionManager from './SessionManager.vue'
import SessionStatus from './SessionStatus.vue'

export default {
    components: {
        SessionManager,
        SessionStatus
    },
    methods: {
        get_token() {
            var get_token_payload = {
                tsew_command: 'get_token',
                clientId: "user@trend.account.email",
                supportId: "michael_mao@trendmicro.com",
                initArg: {
                    removeDownloadFolder: 1,
                    removeUploadFolder: 1
                },
                AirSupportTibcoUrl: "@AirSupportTibcoUrl@",
                countryCode: "JP"
            }
            this.$store.commit('get_token', get_token_payload)
        },
        sendMsg() {
            var payload = {
                clientId: this.$store.clientId,
                supportId: this.$store.supportId,
                token: this.$store.token,
                sessionId: this.$store.token,
                seq: this.$store.sessionId,
                content: {
                    msgId: "50397190",
                    content: {
                        desc: "Send message test",
                        ratio: 90,
                        mode: 0,
                        confirmation: ""
                    }
                }
            }
            this.$store.commit('sendMsg', this.msg)
            this.msg = ''
        }
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
