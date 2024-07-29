const DashboardAdmin = {
  template: `
    <div>
        <h1> Admin Dashboard </h1>
        <h2> Inactive Instructors </h2>
        <div v-for="user in inactiveInst">
            <div class="justify"> <span> email : {{user.email}} </span> <span> <button class="btn btn-secondary" @click="activate(user.id)"> Activate </button> </span> </div>
        </div>
    </div>
  `,
  data() {
    return {
      inactiveInst: [],
    };
  },
  methods: {
    async activate(id) {
      const res = await fetch(window.location.origin + "/activate-inst/" + id, {
        headers: {
          AuthenticationToken: sessionStorage.getItem("token"),
        },
      });

      if (res.ok) {
        alert("instructor activated");
      }
    },
  },
  async mounted() {
    const res = await fetch(window.location.origin + "/inactive_instructors", {
      headers: {
        AuthenticationToken: sessionStorage.getItem("token"),
      },
    });

    if (res.ok) {
      this.inactiveInst = await res.json();
    }
  },
};

export default DashboardAdmin;
