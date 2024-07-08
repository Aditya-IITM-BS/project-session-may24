// import Navbar from "../components/Navbar.js";
import Home from "../pages/Home.js";
import Login from "../pages/Login.js";
import Signup from "../pages/Signup.js";
import Logout from "../pages/Logout.js";
import DashboardStud from "../pages/DashboardStud.js";
import Profile from "../pages/Profile.js";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/signup", component: Signup },
  { path: "/logout", component: Logout },
  { path: "/dashboard", component: DashboardStud },
  { path: "/profile", component: Profile },
];

const router = new VueRouter({
  routes,
});

export default router;
