<template>
    <div :class="isHide()">
        <div class="panel-heading bluma">
            <i class="fa fa-weixin white" aria-hidden="true"></i>
            <span class="white">Chat</span>
            <i class="fa fa-window-minimize white min panel-button" aria-hidden="true" @click="min"></i>
        </div>
        <VisitorInfo />
        <VisitorChat />
    </div>
    </div>
</template>
<script>
import VisitorInfo from './VisitorInfo.vue'
import VisitorChat from './VisitorChat.vue'
export default {
    components: {
        VisitorInfo,
        VisitorChat
    },
    methods: {
        isHide() {
            if (this.$store.state.showStarter)
                return 'panel panel-bluma room hide'
            else
                return 'panel panel-bluma room'
        },
        min() {
            this.$store.commit('switchStarter', true)
        }
    }
}
</script>
<style>
.room {
    width: 300px;
    position: fixed;
    right: 10px;
    bottom: 0px;
}

.min {
    margin-left: 180px
}

.clo {
    margin-left: 10px
}

.icon-padding {
    margin-left: -30px;
}
</style>
