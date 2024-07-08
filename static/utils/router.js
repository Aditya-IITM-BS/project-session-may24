// import Navbar from "../components/Navbar.js";
import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";
import Logout from "../pages/Logout.js";
import DashboardStud from "../pages/DashboardStud.js";
import NotFound from "../components/NotFound.js";

import store from "./store.js";

Vue.use(VueRouter);

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/logout", component: Logout },
  { path: "/dashboard", component: DashboardStud /*, meta: { role: "stud" }*/ },
  { path: "*", component: NotFound },
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  const userRole = store.state.role;
  if (to.meta.role && userRole != to.meta.role) {
    next("/");
  } else {
    next();
  }
});

export default router;
