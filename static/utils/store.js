const store = new Vuex.Store({
  state: {
    authToken: localStorage.getItem("authToken") || "",
    test: "to test vuex working",
    user: null, // User profile data can be stored here
  },
  mutations: {
    setAuthToken(state, token) {
      state.authToken = token;
      localStorage.setItem("authToken", token); // Persist token in local storage
    },
    setUser(state, user) {
      state.user = user;
    },
    logout(state) {
      state.authToken = "";
      localStorage.removeItem("authToken"); // Remove token from local storage on logout
      state.user = null;
    },
  },
  actions: {
    // Actions to fetch user data, handle authentication, etc.
  },
  getters: {
    isLoggedIn: (state) => !!state.authToken,
  },
});

export default store;
