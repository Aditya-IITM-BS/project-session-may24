const Logout = {
  template: `
    <div> 
        <h1 v-if="logoutSuccess">Successful Logged out </h1>
        <h1 v-else> Logout Unsuccessful</h1>
    </div>
    `,
  data() {
    return {
      logoutSuccess: false,
    };
  },
  methods: {
    async created() {
      console.log("Logout created lifecycle hit!! ");

      res = await fetch(window.location.origin + "/logout");
      if (res.ok) {
        this.logoutSuccess = True;
      }
    },
  },
};

export default Logout;
