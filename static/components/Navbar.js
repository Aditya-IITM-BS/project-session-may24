const Navbar = {
  template: `
    <nav class="h3 w-auto d-flex justify-content-between">
    <router-link to='/'>Home</router-link>
    <router-link to='/login'>Login</router-link>
    <router-link to='/signup'>Signup</router-link>
    <a :href="url">Logout</a>
    </nav>
    `,
  data() {
    return {
      url: window.location.origin + "/logout",
    };
  },
};

export default Navbar;
