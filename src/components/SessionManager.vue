<template>
    <div class="btn-group">
        <button type="button" class="btn btn-danger">Manage</button>
        <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="caret"></span>
            <span class="sr-only">Toggle Dropdown</span>
        </button>
        <ul class="dropdown-menu">
            <li><a href="#" @click="get_token">Get TokenID</a></li>
            <li><a href="#">Disconnect</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Test</a></li>
        </ul>
    </div>
</template>
<script>
export default {
    methods: {
        get_token() {
            var get_token_payload = {
                tsew_command: 'get_token',
                clientId: "user@trend.account.email",
                supportId: "michael_mao@trendmicro.com",
                initArg: {
                    removeDownloadFolder: 1,
                    removeUploadFolder: 1
                },
                AirSupportTibcoUrl: "@AirSupportTibcoUrl@",
                countryCode: "JP"
            }
            this.$store.commit('get_token', get_token_payload)
        },
    }
}
</script>
