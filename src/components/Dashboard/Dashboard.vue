<template>
    <div>
        <SideNavBar />
        <MainContainer />
        <AgentChatRoom />
    </div>
</template>
<script>
import SideNavBar from './SideNavBar'
import MainContainer from './MainContainer'
import AgentChatRoom from './AgentChatRoom'

export default {
    components: {
        SideNavBar,
        MainContainer,
        AgentChatRoom
    }
}
</script>
