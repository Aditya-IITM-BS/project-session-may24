import Login from "../pages/Login.js";
import Home from "../pages/home.js";
import Profile from "../pages/Profile.js";
import Signup from "../pages/Signup.js";
// import Logout from "./pages/Logout.js";

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  // { path: "/logout", component: Logout },
  { path: "/profile", component: Profile },
  { path: "/signup", component: Signup },
];

const router = new VueRouter({
  routes,
});

export default router;
