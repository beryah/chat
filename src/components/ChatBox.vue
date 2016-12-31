<template>
	<div class='a'> 
		<p>status: {{ this.$store.state.status}}</p>
    <p>toekn: {{ this.$store.state.token }}</p>    
    <p>clientid: {{ this.$store.state.clientId }}</p>    
    <input type='text' v-model="msg"/>
		<input type='button' value='get token' @click='get_token'/>
	</div>	
</template>
<script>
/* eslint-disable */
export default {
  data() {
  	return{
  		msg: ''
  	}
  },
  methods: {
    get_token () {      
      this.$store.commit('update_connect_status', 'wait for connect')      
      this.$store.commit('get_token', this.msg)
    },
  }
}
</script>
<style>
.a{	
	height: 400px;
	width: 400px;
	border: 1px solid #000;
}
</style>