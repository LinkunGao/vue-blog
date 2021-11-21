import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

// 引入summernote
import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "popper.js";
import "summernote";
import "summernote/dist/summernote.css";
// 导入中文国际化
import "summernote/lang/summernote-zh-CN.js";
import "./assets/css/mystyle.css";

Vue.use(ElementUI);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
