// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'babel-polyfill'
import Vue from 'vue'
import store from './store'
import App from './components/App.vue'
import 'jquery'
import 'socket.io-client';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import './css/chatmo.css';
import moment from 'moment'

/* eslint-disable no-new */

new Vue({
  el: '#app',
  store,
  render: h => h(App)
})
