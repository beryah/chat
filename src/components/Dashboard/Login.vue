<template>
    <div class="container">
        <div class="row">
            <div class="login-t login-tmp">
                <i class="fa fa-weixin m-co" aria-hidden="true"></i>
            </div>
            <br>
            <br><br>
        </div>
        <div class="row">
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
                    <button type="submit" class="btn btn-success l-b">Sign In</button>
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

.login-t {
    text-align: center;
}

.l-b {
    width: 100%
}
</style>
