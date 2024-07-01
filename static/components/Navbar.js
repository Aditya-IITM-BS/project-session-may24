import store from "../utils/store.js";

const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
    <router-link to='/'>Home</router-link>
    <router-link v-if="!computedlog" to='/login'>Login</router-link>
    <router-link v-if="!computedlog" to='/signup'>Signup</router-link>
    <router-link v-if="computedlog" to='/dashboard'>Dashboard</router-link>
    <a v-if="computedlog" :href="url">Logout</a>
    </nav>
    `,
  data() {
    return {
      loggedIn: store.state.loggedIn,
      url: window.location.origin + "/logout",
    };
  },
  computed: {
    computedlog() {
      return store.state.loggedIn;
    },
  },
};

export default Navbar;
