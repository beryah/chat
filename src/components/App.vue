<template>
    <div id="app">
        <HeaderNavBar />
        <MainContainer />
        <VisitorChatWidget />
        <FooterNavBar />
        
    </div>
</template>
<script>
/* eslint-disable */
import HeaderNavBar from './HeaderNavBar.vue'
import MainContainer from './MainContainer.vue'
import VisitorChatWidget from './VisitorChatWidget.vue'
import FooterNavBar from './FooterNavBar.vue'

export default {
    components: {
        HeaderNavBar,
        MainContainer,
        VisitorChatWidget,
        FooterNavBar
    }
}
</script>
