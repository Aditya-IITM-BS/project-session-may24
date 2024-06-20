const Navbar = {
  template: `
        <nav class= "h3 w-auto d-flex justify-content-around ">
            <router-link to='/'>Home</router-link>
            <router-link  to='/profile'>Profile</router-link>
            <router-link  to='/stud-dashboard'>Dashboard</router-link>
            <router-link v-show="!loggedIn" to='/login'>Login</router-link>
            <router-link v-show="!loggedIn" to='/Signup'>Signup</router-link>
            <a :href="logoutURL">Logout</a>
        </nav>
    `,
  data() {
    return {
      loggedIn: false,
      logoutURL: window.location.origin + "/logout",
    };
  },
};

export default Navbar;
