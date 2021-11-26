import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "../store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    // 路由鉴权
    beforeEnter: (to, from, next) => {
      if (store.state.userInfo.token) {
        next();
      } else {
        next("/login");
      }
    },
  },
  {
    path: "/add-article",
    name: "AddArticle",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AddArticle.vue"),
    // 路由鉴权
    beforeEnter: (to, from, next) => {
      if (store.state.userInfo.token) {
        next();
      } else {
        next("/login");
      }
    },
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Login.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Register.vue"),
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

// 重新配置router，以避免报错
const routerPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location).catch((err) => err);
};

const router = new VueRouter({
  routes,
});

// 必须放在这个位置
// 路由管理方案2:全局路由
router.beforeEach((to, from, next) => {
  console.log(to.path);
  console.log(from.path);
  next();
});

export default router;
