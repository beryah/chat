<template>
    <div class="panel-body fixed-panel">
        <p v-for="message in messages" v-bind:class="{alignRight : message.fromClient}">
            <span v-if="message.fromClient">
            	{{ message.content }} :
            	<span class="glyphicon glyphicon-user client"></span>
            </span>
            <span v-else>
            	<span class="glyphicon glyphicon-headphones support"></span>
            	: {{ message.content }}
            </span>
        </p>
    </div>
</template>
<script>
export default {
    props: ['messages']
}
</script>
<style>
.fixed-panel {
    min-height: 200;
    max-height: 200;
    overflow-y: scroll;
}
.client{
	color: #5cb85c;
}
.support{
	color:red;
}
.alignRight{
	text-align: right;
}
</style>
