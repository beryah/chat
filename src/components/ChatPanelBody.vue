<template>
    <div class="panel-body fixed-panel">
        <p v-for="message in messages" v-bind:class="{alignRight : message.fromClient, 'section': true}">
            <span v-if="message.fromClient">
            	<span class="clientTime">{{ message.formatedTime }}</span>            	
            	<span class="glyphicon glyphicon-user clientAvatar"></span>
            	<strong>
            		<p class="msgClient" v-html="message.content"></p>
            	</strong>
            </span>
            <span v-else>
            	<span class="glyphicon glyphicon-headphones supportAvatar">             	
            	</span> 
            	<span class="time">{{ message.formatedTime }}</span>
            	<strong>
            		<p v-bind:class="{msgSupport:true, notArrived: !message.arrived}" v-html="message.content"></p>
            	</strong>
            </span>            
        </p>
    </div>
</template>
<script>
export default {
    props: ['messages'],
}
</script>
<style>
.fixed-panel {
    min-height: 500px;
    max-height: 500px;
    width:60%;
    overflow-y: scroll;
}
.notArrived{
	opacity:0.3;
}
.clientAvatar  {
    color: #5cb85c;
}

.supportAvatar {
    color: red;
}

.alignRight {
    text-align: right;
}
.msgClient{
	font-size: 19px;
	margin-right: 25px;

}
.msgSupport{
	font-size: 19px;
	margin-left: 25px;

}
.time{
	margin-left: 5px;
	color:#777;
}
.clientTime{
	margin-right: 5px;
	color:#777;
}
.section{
	margin-bottom: 10px;
}
</style>
