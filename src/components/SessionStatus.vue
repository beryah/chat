<template>
    <span class="sessionStatusMain">
	        <span class="well"><strong>ID:</strong> {{ session.token }}</span>
    <span class="well"><strong>Connected at:</strong> {{ session.connectedStartTime }}</span>
    <span class="well"><strong>Ver:</strong> {{ session.version }}</span>
    <span class="well" style="color:red">
    	<span class="glyphicon glyphicon-record"></span>
    	{{ session.connectedStatus }}</span>
    </span>
</template>
<script>
export default {
    props: ['session']
}
</script>
<style>
.sessionStatusMain {
    margin-left: 20px;
}
</style>
