<template>
    <div :class="showHide()">
        <VisitorChatMessage />
        <div class="panel-footer icon-bar">
            <i class="fa fa-volume-up fa-lg  icon-gray pointer" style="padding-right:15px" aria-hidden="true"></i>
            <i class="fa fa-paperclip fa-lg icon-gray pointer fa-rotate-90" aria-hidden="true"></i>
            <i class="fa fa-envelope-o fa-lg icon-gray pointer" style="padding-left:15px" aria-hidden="
            true"></i>
            <div class="text-right">
                <i class="fa fa-thumbs-up fa-lg icon-gray pointer" aria-hidden="true"></i>
                <i class="fa fa-thumbs-down fa-lg icon-gray pointer" style="padding-left:7px" aria-hidden="true"></i>
            </div>
        </div>
        <div>
            <textarea class="form-control no-resize" rows="3 " v-model="msg" v-on:keydown="keydown($event)"></textarea>
        </div>
    </div>
</template>
<script>
import VisitorChatMessage from './VisitorChatMessage.vue'

export default {
    components: {
        VisitorChatMessage
    },
    methods: {
        keydown(e) {
            var keycode = e.keyCode || e.which;
            if (keycode === 13 && !e.shiftKey) {
                this.$store.commit('chat', {
                    msg: this.msg,
                    from: 'visitor',
                    roomId: this.$store.state.visitorSocketId
                })
                this.msg = ''
                e.preventDefault();
            }
            var snd = new Audio("file.wav"); 
            snd.play();
        },
        onSubmit() {
            console.log(2)
            return;
        },
        showHide() {
            if (this.$store.state.showVisitorInfo)
                return 'hide'
            else
                return ''
        }
    },
    data() {
        return {
            msg: ''
        }
    },
}
// var audio = new Audio('a.mp3');
// audio.play();
</script>
