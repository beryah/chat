<template>  
  <div id="app">
    <Head />
    <ChatBox />
    <Foot />
  </div>  
</template>

<script>
/* eslint-disable */
import Head from './Head.vue'
import Foot from './Foot.vue'
import ChatBox from './ChatBox.vue'

export default {
  components: {
    Head,
    Foot,
    ChatBox
  },
  methods: {
    increment () {      
      this.$store.commit('increment')
    },
    decrement () {      
      this.$store.commit('decrement')
    }
  }
}
</script>