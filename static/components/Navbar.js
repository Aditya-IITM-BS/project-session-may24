const Navbar = {
  template: `
        <nav class= "h3 w-auto d-flex justify-content-around ">
            <router-link to='/'>Home</router-link>
            <router-link to='/login'>Login</router-link>
            <router-link to='/signup'>Signup</router-link>
            <a :href="logoutURL">Logout</a>
        </nav>
    `,
  data() {
    return {
      logoutURL: window.location.origin + "/logout",
    };
  },
};

export default Navbar;
