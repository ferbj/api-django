import Vue from "vue";
import VueRouter from "vue-router";

import Country from "../views/Country.vue";
import Graphics from "../views/Graphics.vue";
Vue.use(VueRouter);

const routes = [{
        path: "/country",
        name: "Country",
        component: Country
    },
    {
        path: "/graphics",
        name: "Graphics",
        component: Graphics
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;