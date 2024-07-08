Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    loggedIn: false,
    role: null,
  },

  mutations: {
    setLogin(state) {
      state.loggedIn = true;
    },
    logout(state) {
      state.loggedIn = false;
      state.role = null;
    },
    setRole(state, role) {
      state.role = role;
    },
  },
});

export default store;
