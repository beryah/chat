<template>
    <div :class="showHide()">
        <div class="panel-body chat-body">
            <p class="msg-system">aaaa join</p>
            <div class="msg-me">
                <span>hello, I am Michael and I need your help</span>
            </div>
            <div class="msg-agent">
                <span>msg from agent</span>
            </div>
             <div class="msg-me">
                <span>hello, I am Michael and I need your help</span>
            </div>
            <div class="msg-agent">
                <span>msg from agent</span>
            </div>
             <div class="msg-me">
                <span>hello, I am Michael and I need your help</span>
            </div>
            <div class="msg-agent">
                <span>msg from agent</span>
            </div>
             <div class="msg-me">
                <span>hello, I am Michael and I need your help</span>
            </div>
            <div class="msg-agent">
                <span>msg from agent</span>
            </div>
        </div>
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
export default {
    components: {},
    methods: {
        keydown(e) {
            var keycode = e.keyCode || e.which;
            if (keycode === 13 && !e.shiftKey) {
                this.$store.commit('chat', {
                    msg: this.msg,
                    from: 'me'
                })
                this.msg = ''
                e.preventDefault();
            }
        },
        onSubmit() {
            console.log(2)
            return;
            // var keycode = e.keyCode || e.which;

            // if (keycode === 13 && !e.shiftKey) {
            //     this.$store.commit('chat', {
            //         msg: msg,
            //         fromUser: true
            //     })
            //     this.msg = ''
            // }
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
</script>
<style>
.chat-body {
    height: 200px;
    width: 100%;
    overflow-y: scroll;
    overflow-x: hidden;
    display: block;
}

.usermsg {
    background-color: #BEF18C;
    text-align: right;
}

.agentmsg {
    background-color: #E4E8EB;
}

.systemmsg {
    text-align: center;
}

.icon-bar {
    background-color: #F6F6F6;
}
</style>
