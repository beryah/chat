<template>
    <div :class="showHide()">
        <form @submit.prevent="onSubmit" >
            <div class="form-group">
                <input type="text" class="form-control" placeholder="* Name" v-model="name">
            </div>
            <div class="form-group">
                <input type="email" class="form-control" id="exampleInputEmail1" placeholder="* Email">
            </div>
            <button type="submit" class="btn bluma white">Start Chat</button>
        </form>
    </div>
</template>
<script>
export default {
    methods: {
        onSubmit() {
            this.$store.commit('switchVisitorInfo', false)
            this.$store.commit('visitorJoin', this.name)
        },
        showHide() {
            if (this.$store.state.showVisitorInfo)
                return 'panel-body'
            else
                return 'panel-body hide'
        }
    },
    data() {
        return {
            name: ''
        }
    }
}
</script>
