<template>  
  <div id="app">
    <Header />
    <ChatBox />
    <p>{{ this.$store.state.count}}</p>
    <p>
      <button @click="increment">+</button>
      <button @click="decrement">-</button>
    </p>
    <Footer />
  </div>  
</template>

<script>
import Header from './Header.vue'
import Footer from './Footer.vue'
import ChatBox from './ChatBox.vue'
import io from 'socket.io-client'

var socket = io('localhost:50013')

export default {
  components: {
    Header,
    Footer,
    ChatBox
  },
  methods: {
    increment () {
      socket.emit('chat message')
      this.$store.commit('increment')
    },
    decrement () {
      this.$store.commit('decrement')
    }
  }
}
</script>