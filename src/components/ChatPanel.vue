<template>
<div>
  <ul class="nav nav-tabs" role="tablist">
    <li role="user1" class="active"><a href="#home" aria-controls="home" role="tab" data-toggle="tab">User1</a></li>
    <li role="user2"><a href="#profile" aria-controls="profile" role="tab" data-toggle="tab">User2</a></li>
    <li role="user3"><a href="#messages" aria-controls="messages" role="tab" data-toggle="tab">User3</a></li>
    <li role="user4"><a href="#settings" aria-controls="settings" role="tab" data-toggle="tab">User4</a></li>
  </ul>

  <div class="tab-content">
  	<div role="tabpanel" class="tab-pane active panel panel-default" id="home">	  	  		  		
	  	<div class="panel panel-default">
	  		<div class="panel-body">
	  			<span>ID: {{ this.$store.state.token }}</span>
	  			<span>Session ID: {{ this.$store.state.sessionId }}</span>
	  			<span>support ID: {{ this.$store.state.supportId }}</span>
	  			<span>seq{{ this.$store.state.seq }}</span>
	  		</div>
	  		<div class="panel-footer">
	  			<div class="input-group">		      
			      <input type="text" class="form-control" placeholder="Search for..." v-model="msg">
			      <span class="input-group-btn">
			        <button class="btn btn-success" type="button" @click='sendMsg'>Send</button>
			      </span>
			    </div><!-- /input-group -->
	  		</div>
		</div>
	</div>
    <div role="tabpanel" class="tab-pane" id="profile">..2.</div>
    <div role="tabpanel" class="tab-pane" id="messages">.3..</div>
    <div role="tabpanel" class="tab-pane" id="settings">..4.</div>
  </div>
 </div>
</template>
<style>
	.panel-body{
		height: 200px;
	}
</style>
<script>
	export default{
		data() {
  			return{
  				msg: ''
  			}
  		},
		methods: {
			sendMsg(){
				var payload = {
					clientId:this.$store.clientId,
					supportId:this.$store.supportId,
					token:this.$store.token,
					sessionId:this.$store.token,
					seq:this.$store.sessionId,
					content:{
						msgId:"50397190 ",
						content:{
							desc:"Send message test",
							ratio:90,
							mode:0,
							confirmation:""
						}
					}
				}
				this.$store.commit('sendMsg',this.msg)
				this.msg = ''
		 	}
		}
	}
</script>