<template>
    <div class="btn-group">
        <button type="button" class="btn btn-danger">Manage</button>
        <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="caret"></span>
            <span class="sr-only">Toggle Dropdown</span>
        </button>
        <ul class="dropdown-menu">
            <li><a href="#" @click="registerToken">Get TokenID</a></li>
            <li><a href="#" @click="terminate">Disconnect</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Test</a></li>
        </ul>
    </div>
</template>
<script>
export default {
    methods: {
        registerToken() {
            var payload = {
                clientId: "user@trend.account.email",
                supportId: "michael_mao@trendmicro.com",
                initArg: {
                    removeDownloadFolder: 1,
                    removeUploadFolder: 1
                },
                AirSupportTibcoUrl: "@AirSupportTibcoUrl@",
                countryCode: "JP"
            }
            this.$store.commit('getToken', payload)
        },
        terminate() {
            var payload = {
                token: this.$store.state.sessions[0].token,
                sessionId: this.$store.state.sessions[0].sessionId,
                clientId: this.$store.state.sessions[0].clientId,
                supportId: this.$store.state.sessions[0].supportId
            }
            this.$store.commit('terminate', payload)
        }
    }
}
</script>
