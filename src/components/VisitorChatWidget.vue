<template>
    <div>
        <VisitorChatStarter @click.native="hideStarter" />
        <VisitorChatRoom />
    </div>
</template>
<script>
import VisitorChatStarter from './VisitorChatStarter.vue'
import VisitorChatRoom from './VisitorChatRoom.vue'

export default {
    components: {
        VisitorChatStarter,
        VisitorChatRoom
    },
    methods: {
        hideStarter() {
            this.$store.commit('switchStarter', false)
        },
    }
}
</script>
