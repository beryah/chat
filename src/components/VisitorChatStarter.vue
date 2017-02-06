<template>
    <div :class="getStarterClass()">
        <div class="panel-heading">
            <i class="fa fa-weixin white" aria-hidden="true"></i>
            <span class="white">Start Chat</span>
        </div>
    </div>
</template>
<script>
export default {
    methods:{
        getStarterClass(){
            if(this.$store.state.showStarter)
                return 'bluma starter'
            else
                return 'bluma starter hide' 
        }
    }
}
</script>
<style>
.starter {
    width: 200px;
    position: fixed;
    right: 10px;
    bottom: 0px;
    cursor: pointer;
}
</style>
