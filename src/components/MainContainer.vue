<template>
	<div class="main_container">
		<button type="button" class="btn btn-primary" @click="get_token">Get TokenID</button>
    	<ChatPanel />
	</div>
</template>    
<script>
import ChatPanel from './ChatPanel.vue'

export default {
	components:{
		ChatPanel
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
    	}
    }
}
</script>
<style>
	.main_container{
		margin-left: 220px;
	}
</style>