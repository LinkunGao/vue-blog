import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: {},
  },
  // 仅支持同步操作
  mutations: {
    // 保存注册登陆用户信息
    saveUserInfo(state, userInfo) {
      state.userInfo = userInfo;
    },
  },
  // 仅支持异步操作
  actions: {},
  modules: {},
});
