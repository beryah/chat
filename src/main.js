// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'babel-polyfill'
import Vue from 'vue'
import store from './store'
import App from './components/App.vue'
import Dashboard from './components/Dashboard/Dashboard.vue'
import Home from './components/Home.vue'
import 'jquery'
import 'socket.io-client';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import VueRouter from 'vue-router';
import './css/chatmo.css';
import moment from 'moment'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', component: Home },
    { path: '/Dashboard', component: Dashboard },
  ]
})

new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
})
