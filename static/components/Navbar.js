const Navbar = {
  template: `
        <nav class= "h3 w-auto d-flex justify-content-around">
            <router-link to='/'>Home</router-link>
            <router-link to='/login'>Login</router-link>
            <router-link to='/Signup'>Signup</router-link>
            <router-link to='/Logout'>Logout</router-link>
        </nav>
    `,
};

export default Navbar;
