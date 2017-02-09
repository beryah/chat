<template>
    <div :class="isHide()">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
                    <h4 class="modal-title" id="exampleModalLabel">temp</h4> </div>
                <div class="modal-body">
                    <div v-for="(chat,index) in this.$store.state.messages" :class="messageStyle(chat)">
                        <span>{{chat.msg}}</span>
                    </div>
                </div>
                <textarea class="form-control no-resize" rows="3 " v-model="msg" v-on:keydown="keydown($event)"></textarea>
            </div>
        </div>
    </div>
</template>
<script>
export default {

    components: {

    },
    methods: {
        isHide() {
            if (this.$store.state.showAgentChatRoom)
                return 'overlay'
            else
                return 'overlay hide'
        },
        keydown(e) {
            var keycode = e.keyCode || e.which;
            if (keycode === 13 && !e.shiftKey) {
                this.$store.commit('chat', {
                    msg: this.msg,
                    from: 'agent'
                })
                this.msg = ''
                e.preventDefault();
            }
        },
        onSubmit() {
            console.log(2)
            return;
        },
        messageStyle(chat) {
            console.log(chat.from)
            if (chat.from == 'visitor')
                return 'msg-visitor'
            if (chat.from == 'system')
                return 'msg-system'
            if (chat.from == 'agent')
                return 'msg-agent'
        },
    },
    data() {
        return {
            msg: ''
        }
    },
}
</script>
<style>
.overlay {
    top: 0px;
    position: fixed;
    z-index: 9999;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
}

.agent-room {
    height: 80%;
    background-color: #fff;
    opacity: 0;
}
</style>
