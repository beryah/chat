<template>
    <div class="panel-body chat-body">
        <div v-for="(chat,index) in this.$store.state.messages" :class="messageStyle(chat)">
            <span>{{chat.msg}}</span>
        </div>
    </div>
</template>
<script>
export default {
    updated: function() {
        this.$el.scrollTop = this.$el.scrollHeight
    },
    methods: {
        messageStyle(chat) {
            console.log(chat.from)
            if (chat.from == 'visitor')
                return 'msg-visitor'
            if (chat.from == 'system')
                return 'msg-system'
            if (chat.from == 'agent')
                return 'msg-agent'
        },
    }
}
</script>
<style>
.chat-body {
    height: 200px;
    width: 100%;
    overflow-y: scroll;
    overflow-x: hidden;
    display: block;
}
</style>
