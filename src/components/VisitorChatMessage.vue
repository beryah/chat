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
            if (chat.from == 'me')
                return 'msg-me'
            if (chat.from == 'system')
                return 'msg-system'
            if (chat.from == 'agent')
                return 'msg-agent'

        },
    }
}
</script>
