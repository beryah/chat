<template>
    <div id="app">
        <NavBar />
        <LeftNavBar />
        <MainContainer />
    </div>
</template>
<script>
/* eslint-disable */
import NavBar from './NavBar.vue'
import ChatPanel from './ChatPanel.vue'
import Foot from './Foot.vue'
import LeftNavBar from './LeftNavBar.vue'
import MainContainer from './MainContainer.vue'

export default {
    components: {
        NavBar,
        LeftNavBar,
        MainContainer,
        ChatPanel,
        Foot
    }
}
</script>
