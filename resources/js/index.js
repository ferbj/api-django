import Vue from 'vue'
import App from './App.vue'

import router from './router'
import axios from 'axios'
import VueCookies from 'vue-cookies'
import * as bootstrap from 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false
import JwPagination from 'jw-vue-pagination';


window.Popper = require('popper.js').default;
window.$ = window.jQuery = require('jquery');

window.axios = axios;
Vue.component('paginate', JwPagination);

Vue.use(bootstrap);
Vue.use(VueCookies);

let csrftoken = $cookies.get('csrftoken');
window.axios.defaults.xsrfCookieName = 'csrftoken';
//window.axios.defaults.headers.common['Access-Control-Request-Method'] = '*';

//window.axios.defaults.headers.common['X-CSRFToken'] = csrftoken;
/*window.axios.defaults.xsrfHeaderName = "X-CSRFToken"
window.axios.defaults.headers.common['x-csrftoken'] = csrftoken;
window.axios.defaults.headers.common.accept = 'application/json'*/
new Vue({
    router,
    components: {
    App
    },
    render: h => h(App)
  }).$mount('#app')

