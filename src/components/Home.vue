<template>
    <div>
        <HeaderNavBar />
        <MainContainer />
        <VisitorChatWidget />
<!--           <audio id='myAudio' controls autoplay loop>
            <source src="../static/briefcase-lock.mp3" type="audio/mpeg"> Your browser does not support the audio element.
        </audio>  -->
        <!-- <img src="../assets/a.mp3"> -->
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
