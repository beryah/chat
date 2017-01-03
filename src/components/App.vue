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
import ChatBox from './ChatBox.vue'
import LeftNavBar from './LeftNavBar.vue'
import MainContainer from './MainContainer.vue'

export default {
  components: {
    NavBar,
    LeftNavBar,
    MainContainer,
    ChatPanel,
    Foot,
    ChatBox
  },
  methods: {
    get_token () {            
     var get_token_payload = {
      tsew_command: 'get_token',
      clientId:"user@trend.account.email",
      supportId:"michael_mao@trendmicro.com",
      initArg:{
          removeDownloadFolder:1,
          removeUploadFolder:1
        },
        AirSupportTibcoUrl:"@AirSupportTibcoUrl@",
        countryCode:"JP"
      }
      this.$store.commit('get_token', get_token_payload)
    },
    increment () {      
      this.$store.commit('increment')
    },
    decrement () {      
      this.$store.commit('decrement')
    }
  }
}
</script>