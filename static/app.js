// import components
import Home from "./pages/home.js";

const routes = [{ path: "/", component: Home }];

const router = new VueRouter({
  routes,
});

new Vue({
  el: "#app",
  router,
  template: `
        <div>
        <router-view></router-view>
        </div>
    `,
});
