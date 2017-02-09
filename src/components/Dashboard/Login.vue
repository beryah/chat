<template>
    <div class="container">
        <div class="row login-tmp">
            <div class="col-md-4">
            </div>
            <div class="col-md-4">
                <form @submit.prevent="onSubmit">
                    <div class="form-group">
                        <input v-model="name" type="input" class="form-control" placeholder="User Name">
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" placeholder="Password">
                    </div>
                    <button type="submit" class="btn btn-success">Sign In</button>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        onSubmit() {
            this.$store.commit('agentJoin', this.name)
            this.$router.push('/Dashboard')
        }
    },
    data() {
        return {
            name: ''
        }
    }
}
</script>
<style>
.login-tmp {
    margin-top: 200px;
}
</style>
