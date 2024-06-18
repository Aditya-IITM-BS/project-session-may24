const Login = {
  template: `
    <div class="d-flex justify-content-center align-items-center">
      <div class="h-25 w-25 border border-2 d-flex flex-column">
        <input v-model="email" placeholder="email"/>
        <input v-model="password" type="password" placeholder="password"/>
        <button class="btn btn-primary w-max-25" @click="submitInfo">Submit</button>
      </div>
    </div>
  `,
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async submitInfo() {
      const origin = window.location.origin;
      const url = `${origin}/login`;
      const res = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: this.email, password: this.password }),
        credentials: "same-origin", // Include credentials (cookies) with the request
      });

      if (res.ok) {
        const data = await res.json();
        console.log(data);
        // Handle successful login, e.g., redirect or store token
      } else {
        const errorData = await res.json();
        console.error("Login failed:", errorData);
        // Handle login error, e.g., show error message to user
      }
    },
  },
};

export default Login;
