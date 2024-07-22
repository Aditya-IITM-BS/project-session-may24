// import Navbar from "../components/Navbar.js";
import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";
import Logout from "../pages/Logout.js";
import DashboardStud from "../pages/DashboardStud.js";
import DashboardInst from "../pages/DashboardInst.js";
import DashboardAdmin from "../pages/DashboardAdmin.js";
import Profile from "../pages/Profile.js";

import store from "./store.js";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/logout", component: Logout },
  {
    path: "/dashboard-stud",
    component: DashboardStud,
    meta: { requiresLogin: true, role: "stud" },
  },
  {
    path: "/dashboard-inst",
    component: DashboardInst,
    meta: { requiresLogin: true, role: "inst" },
  },
  {
    path: "/dashboard-admin",
    component: DashboardAdmin,
    meta: { requiresLogin: true, role: "admin" },
  },
  { path: "/profile", component: Profile, meta: { loggedIn: true } },
];

const router = new VueRouter({
  routes,
});

// frontend router protection
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (!store.state.loggedIn) {
      next({ path: "/login" });
    } else if (to.meta.role && to.meta.role !== store.state.role) {
      next({ path: "/" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
