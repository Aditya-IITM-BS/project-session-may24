import router from "../utils/router.js";
// import store from "../utils/store.js";

const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
    <router-link to='/'>Home</router-link>
    <router-link  to='/login'>Login</router-link>
    <router-link  to='/signup'>Signup</router-link>
    <router-link  to='/dashboard'>Dashboard</router-link>
    <router-link  to='/profile'>Profile </router-link>
    <a @click='logout'>Logout</a>
    </nav>
    `,
  data() {
    return {
      url: window.location.origin + "/logout",
    };
  },

  methods: {
    logout() {
      sessionStorage.clear();
      router.push("/home");
    },
  },
};

export default Navbar;
