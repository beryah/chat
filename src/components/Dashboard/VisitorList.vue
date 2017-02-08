<template>
    <ul class="visitor-ul">
        <li v-for="visitor in this.$store.state.visitors">
            <i class="fa fa-weixin white" aria-hidden="true"></i> {{ visitor.name}}
        </li>
    </ul>
</template>
<script>
export default {

    components: {},
    methods: {
        temp() {

        },
    },
    data() {
        return {

        }
    }
}
</script>
