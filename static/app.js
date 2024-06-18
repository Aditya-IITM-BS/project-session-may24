// import components
import Home from "./pages/home.js";
import Navbar from "./components/Navbar.js";
import Login from "./pages/Login.js";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
];

const router = new VueRouter({
  routes,
});

new Vue({
  el: "#app",
  router,
  components: { Navbar },
  template: `
        <div>
        <Navbar/>
        <router-view></router-view>
        </div>
    `,
});
