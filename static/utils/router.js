import store from "./store.js";

// import Navbar from "../components/Navbar.js";y
import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";
import Logout from "../pages/Logout.js";
import DashboardStud from "../pages/DashboardStud.js";
import DashboardInst from "../pages/DashboardInst.js";
import DashboardAdmin from "../pages/DashboardAdmin.js";
import Profile from "../pages/Profile.js";

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
  { path: "/profile", component: Profile, meta: { requiresLogin: true } },
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  // check this

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
