<template>
    <div>
        <SideNavBar />
        <VisitorList />
        <MainContainer />
        <AgentChatRoom />
    </div>
</template>
<script>
import SideNavBar from './SideNavBar'
import MainContainer from './MainContainer'
import AgentChatRoom from './AgentChatRoom'
import VisitorList from './VisitorList.vue'

export default {
    components: {
        SideNavBar,
        MainContainer,
        AgentChatRoom,
        VisitorList
    }
}
</script>
