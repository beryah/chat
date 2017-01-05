<template>
	<div class="main_container">		
    	<ChatPanel />
	</div>
</template>    
<script>
import ChatPanel from './ChatPanel.vue'

export default {
	components:{
		ChatPanel
	}
}
</script>
<style>
	.main_container{
		margin-left: 220px;
	}
</style>