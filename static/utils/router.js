import Login from "../pages/Login.js";
import Home from "../pages/home.js";
import Profile from "../pages/Profile.js";
import Signup from "../pages/Signup.js";
import DashboardAdmin from "../pages/DashboardAdmin.js";
import DashboardInst from "../pages/DashboardInst.js";
import DashboardStud from "../pages/DashboardStud.js";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/profile", component: Profile },
  { path: "/signup", component: Signup },
  { path: "/inst-dashboard", component: DashboardInst },
  { path: "/stud-dashboard", component: DashboardStud },
];

const router = new VueRouter({
  routes,
});

export default router;
