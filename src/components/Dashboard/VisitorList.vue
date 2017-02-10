<template>
    <div class="visitor-ul">
        <a href="#" v-for="(visitor, index) in this.$store.state.visitors" @click="joinUserRoom(visitor.id)">
            {{ visitor.name}}
        </a>
    </div>
    <!--  <ul class="visitor-ul">
        <li v-for="(visitor, index) in this.$store.state.visitors" @click="joinUserRoom(visitor.id)">
            <i class="fa fa-weixin white" aria-hidden="true"></i> {{ visitor.name}}
        </li>
    </ul> -->
</template>
<script>
export default {

    components: {},
    methods: {
        joinUserRoom(id) {
            console.log(id)
            this.$store.commit('joinUserRoom', {
                name: this.$store.state.agentName,
                joinedRoomId: id
            });
            this.$store.state.joinedRoomId = id
            this.$store.state.showAgentChatRoom = true
        },
    },
    data() {
        return {

        }
    }
}
</script>
<style>
.visitor-ul {
    background-color:transparent;
    position: fixed;
    left: 220px;
    bottom: 15px;
    z-index: 9999;
}

.visitor-ul a{
    color:white;
    padding: 10px 30px 10px 30px;
    border-radius: 10px 10px 0px 0px; 
    background-color: orange;
    margin-left: 10px;
}
</style>
