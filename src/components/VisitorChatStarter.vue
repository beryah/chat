<template>
    <div :class="getStarterClass()">
        <!-- <i class="fa fa-arrow-down i-p" aria-hidden="true"></i> -->
        <div class="panel-heading">
            <i class="fa fa-weixin white" aria-hidden="true"></i>
            <span class="white">Start Chat</span>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        getStarterClass() {
            if (this.$store.state.showStarter)
                return 'bluma starter'
            else
                return 'bluma starter hide'
        }
    }
}
</script>
<style>
.i-p {
    color: #00d1b2;
    position: absolute;
    top: -80px;
    left: 70px;
    font-size: 4em;
}

.starter {
    width: 200px;
    position: fixed;
    right: 10px;
    bottom: 0px;
    cursor: pointer;
}
</style>
