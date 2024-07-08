import router from "./utils/router.js";
import Navbar from "./components/Navbar.js";
import store from "./utils/store.js";

Vue.config.devtools = true;

new Vue({
  el: "#app",
  store,
  template: `
  <div>
    <Navbar/>
    <router-view/>
    </div>
    `,
  router,
  components: {
    Navbar,
  },
});
