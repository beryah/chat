<template>
    <div>
        <span>ID: {{ session.token }}</span>
        <span>Session ID: {{ session.sessionId }}</span>
        <span>support ID: {{ session.supportId }}</span>
        <span>seq{{ session.seq }}</span>
    </div>
</template>
<script>
	export default{
		props: ['session']
	}
</script>