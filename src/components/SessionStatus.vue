<template>
    <span class="sessionStatusMain">
            <span class="well"><strong>ID:</strong> {{ session.token }}</span>
    <span class="well"><strong>Connected at:</strong> {{ session.connectedStartTime }}</span>
    <span class="well"><strong>Ver:</strong> {{ session.version }}</span>
    <span v-bind:class="getStatusStyle">
        <span class="glyphicon glyphicon-record"></span> {{ session.connectedStatus }}</span>
    </span>
</template>
<script>
export default {
    props: ['session'],
    computed:{
        getStatusStyle(){
            switch (this.session.connectedStatus){
                case 'Connected':
                    return "well green"
                    break;
                case 'Registing token id':
                    return "well red";
                    break;
                default:
                    return 'well'
            }
                
        }
    }
}
</script>
<style>
.sessionStatusMain {
    margin-left: 20px;
}
.red{
    color:red;
}
</style>
