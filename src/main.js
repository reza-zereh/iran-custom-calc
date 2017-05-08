import './bootstrap.js';

import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import DcnBasics from './components/DcnBasics.vue';
import DcnItemsForm from './components/DcnItemsForm.vue';
import DcnCostsResult from './components/DcnCostsResult.vue';

Vue.use(VueRouter);
window.Event = new Vue();

// TODO: Pass App's `declarationBasics` to child components to mkae vue-router working
const routes = [
  { path: '/', component: DcnBasics },
  { path: '/items', component: DcnItemsForm },
  { path: '/costs-result', component: DcnCostsResult }
];

const router = new VueRouter({
  routes
});

new Vue({
  el    : '#app',
  router: router,
  render: h => h(App)
});