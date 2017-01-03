<template>
<div>
<div>

  <!-- Nav tabs -->
  <ul class="nav nav-tabs" role="tablist">
    <li role="presentation" class="active"><a href="#home" aria-controls="home" role="tab" data-toggle="tab">Home</a></li>
    <li role="presentation"><a href="#profile" aria-controls="profile" role="tab" data-toggle="tab">Profile</a></li>
    <li role="presentation"><a href="#messages" aria-controls="messages" role="tab" data-toggle="tab">Messages</a></li>
    <li role="presentation"><a href="#settings" aria-controls="settings" role="tab" data-toggle="tab">Settings</a></li>
  </ul>

  <!-- Tab panes -->
  <div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="home">..12.</div>
    <div role="tabpanel" class="tab-pane" id="messages">.13..</div>
    <div role="tabpanel" class="tab-pane" id="settings">..123.</div>
  </div>

</div>
  <ul class="nav nav-tabs" role="tablist">
    <li v-for="session in sessions" role="presentation" >
    	<a :href="'#a' +session.token" :aria-controls="'a'+session.token" role="tab" data-toggle="tab">
    		{{session.token}}
    	</a>
    </li>
  </ul>

  <div class="tab-content">
  	<div v-for="session in sessions"  class="tab-pane active" :id="'a'+session.token" role="tabpanel">
	  	<div class="panel panel-default">
	  		<div class="panel-body">
	  			<span>ID: {{ session.token }}</span>
	  			<span>Session ID: {{ session.sessionId }}</span>
	  			<span>support ID: {{ session.supportId }}</span>
	  			<span>seq{{ session.seq }}</span>
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
		},
		computed:{
			sessions() {
				return this.$store.state.sessions;
			}
		}
	}
</script>