import router from "../utils/router.js";
// import store from "../utils/store.js";

const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
    <router-link to='/'>Home</router-link>
    <router-link v-if="!state.loggedIn" to='/login'>Login</router-link>
    <router-link v-if="!state.loggedIn" to='/signup'>Signup</router-link>
    <router-link v-if="state.loggedIn && state.role === 'stud'" to='/dashboard-stud'>Dashboard</router-link>
    <router-link v-if="state.loggedIn && state.role === 'inst'" to='/dashboard-inst'>Dashboard</router-link>
    <router-link v-if="state.loggedIn && state.role === 'admin'" to='/dashboard-admin'>Dashboard</router-link>
    <router-link v-if="state.loggedIn" to='/profile'>Profile </router-link>
    <a v-if="state.loggedIn" @click='logout'>Logout</a>
    </nav>
    `,
  data() {
    return {
      url: window.location.origin + "/logout",
    };
  },

  computed: {
    state() {
      return this.$store.state;
    },
  },

  methods: {
    logout() {
      sessionStorage.clear();

      this.$store.commit("logout");
      this.$store.commit("setRole", null);

      router.push("/home");
    },
  },
};

export default Navbar;
