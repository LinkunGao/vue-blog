import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import Qs from "qs";
import router from "../router";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: {},
  },
  getters: {
    // 查询登录状态
    isNotUserLogin(state) {
      return state.userInfo.token;
    },
  },
  // 仅支持同步操作
  mutations: {
    // 保存注册登陆用户信息
    saveUserInfo(state, userInfo) {
      state.userInfo = userInfo;
    },
  },
  // 仅支持异步操作
  actions: {
    // 登陆
    blogLogin({ commit }, formData) {
      axios({
        url: process.env.VUE_APP_BASE_URL + "skycoco-login/",
        method: "post",
        data: Qs.stringify(formData),
      })
        .then((res) => {
          if (res.data == "none") {
            alert("username does't exist!");
            return;
          } else if (res.data == "pwderr") {
            alert("wrong password!");
            return;
          }
          //   console.log(res);
          commit("saveUserInfo", res.data);
          router.push({ path: "/" });
        })
        .catch((err) => console.error(err));
    },
    blogRegister({ commit }, formData) {
      axios({
        url: process.env.VUE_APP_BASE_URL + "skycoco-register/",
        method: "post",
        data: Qs.stringify(formData),
      })
        .then((res) => {
          if (res.data == "username_repeat") {
            alert("The username has already exist!");
            return;
          }
          // console.log(res.data);
          commit("saveUserInfo", res.data);
          router.push({ path: "/" });
        })
        .catch((err) => console.error(err));
    },
  },
  modules: {},
});
