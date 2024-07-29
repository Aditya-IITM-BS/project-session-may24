// import { state, logout } from "../utils/state.js";
import router from "../utils/router.js";

const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
      <router-link to="/">Home</router-link>
      <router-link v-if="!state.loggedIn" to="/login">Login</router-link>
      <router-link v-if="!state.loggedIn" to="/signup">Signup</router-link>
      <router-link v-if="state.loggedIn && state.role === 'stud'" to="/dashboard-stud">Dashboard</router-link>
      <router-link v-if="state.loggedIn && state.role === 'inst'" to="/dashboard-inst">Dashboard</router-link>
      <router-link v-if="state.loggedIn && state.role === 'admin'" to="/dashboard-admin">Dashboard</router-link>
      <router-link v-if="state.loggedIn" to="/profile">Profile</router-link>
      <button class="btn btn-warning text-xl" v-if="state.loggedIn" @click="logout">Logout</button>
      </nav>
  `,

  methods: {
    logout() {
      // clear session
      sessionStorage.clear();

      // clear vuex login info
      this.$store.commit("logout");
      this.$store.commit("setRole", null);

      this.$router.push("/");
    },
  },
  computed: {
    state() {
      return this.$store.state;
    },
  },
};

export default Navbar;
