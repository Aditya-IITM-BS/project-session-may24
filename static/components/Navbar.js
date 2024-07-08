import Logout from "../pages/Logout.js";
import router from "../utils/router.js";
import store from "../utils/store.js";

const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
    <router-link to='/'>Home</router-link>
    <router-link v-if="!computedlog" to='/login'>Login</router-link>
    <router-link v-if="!computedlog" to='/signup'>Signup</router-link>
    <router-link v-if="computedlog" to='/dashboard'>Dashboard</router-link>
    <a v-if="computedlog" @click="logout">Logout</a>
    </nav>
    `,
  data() {
    return {
      loggedIn: store.state.loggedIn,
      url: window.location.origin + "/logout",
    };
  },
  methods: {
    logout() {
      localStorage.clear();
      router.push("/home");
    },
  },
  computed: {
    computedlog() {
      return store.state.loggedIn;
    },
  },
};

export default Navbar;
