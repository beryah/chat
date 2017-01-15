<template>
    <div id="app">
<!--         <NavBar />
        <LeftNavBar />
        <MainContainer /> -->
        <TabPnael>
            <Tabs>
                <Tab>
                    <h1>tab1 header</h1>
                </Tab>
                <Tab>
                    <h1>tab2 header</h1>
                </Tab>
            </Tabs>
        </TabPnael>
    </div>
</template>
<script>
/* eslint-disable */
import NavBar from './NavBar.vue'
import ChatPanel from './ChatPanel.vue'
import Foot from './Foot.vue'
import LeftNavBar from './LeftNavBar.vue'
import MainContainer from './MainContainer.vue'
import TabPnael from './TabPanel.vue'
import Tabs from './Tabs.vue'
import Tab from './Tab.vue'

export default {
    components: {
        NavBar,
        LeftNavBar,
        MainContainer,
        ChatPanel,
        Foot,
        TabPnael,
        Tabs,
        Tab
    }
}
</script>
