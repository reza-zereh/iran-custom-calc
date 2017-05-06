import './bootstrap.js';

import Vue from 'vue';
window.Event = new Vue();
import App from './App.vue';

new Vue({
    el: '#app',
    render: h => h(App)
});