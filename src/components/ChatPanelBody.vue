<template>
    <div class="panel-body fixed-panel">
        <p v-for="message in messages">
           <span class="glyphicon glyphicon-user"></span>: {{ message.content }}
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
</style>
