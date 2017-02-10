<template>
    <div>
        <HeaderNavBar />
        <MainContainer />
        <VisitorChatWidget />
        <audio controls autoplay loop>
            <source src="../assets/a.mp3" type="audio/mpeg"> Your browser does not support the audio element.
        </audio>
        <!-- <FooterNavBar /> -->
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
