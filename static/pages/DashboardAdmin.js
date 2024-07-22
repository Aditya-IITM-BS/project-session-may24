const AdminDashboard = {
  template: `
    <div>
        <h1> Admin Dashboard </h1>
        <div v-for="user in inactiveInst">
            <div> {{user.email}} || <button @click="sendApproval(user.id)">Approve</button> </div>
        </div>
    </div>
    `,
  data() {
    return {
      inactiveInst: null,
    };
  },
  methods: {
    async sendApproval(id) {
      const res = await fetch(window.location.origin + "/activate-inst/" + id, {
        headers: {
          AuthenticationToken: sessionStorage.getItem("token"),
        },
      });
    },
  },
  async mounted() {
    const res = await fetch(window.location.origin + "/inactive_instructors", {
      headers: {
        AuthenticationToken: sessionStorage.getItem("token"),
      },
    });

    this.inactiveInst = await res.json();
  },
};

export default AdminDashboard;
