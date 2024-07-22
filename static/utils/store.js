const store = new Vuex.Store({
  state: {
    loggedIn: false,
    role: "",
  },

  mutations: {
    setLogin(state) {
      state.loggedIn = true;
    },
    logout(state) {
      state.loggedIn = false;
    },
    setRole(state, role) {
      state.role = role;
    },
  },
});

export default store;
