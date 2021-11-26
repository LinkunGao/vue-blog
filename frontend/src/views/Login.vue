<template>
  <div id="login-page">
    <div class="dweb loginbox">
      <div class="header">
        User Login
        <el-divider></el-divider>
      </div>
      <el-form :label-position="'right'" label-width="100px" :model="formData">
        <el-form-item label="Username">
          <el-input v-model="formData.username"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="formData.password" type="password"></el-input>
        </el-form-item>
        <el-form-item class="submit-box">
          <el-button @click="blogLogin()" type="success">Sign in</el-button>
          <el-button @click="toRegister()" type="warning">Sign up</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        username: "",
        password: "",
      },
    };
  },
  // 局部路由
  beforeRouteEnter(to, from, next) {
    console.log("路由跳转" + from.path);
    next();
  },
  methods: {
    blogLogin() {
      if (
        this.formData.username.length == 0 ||
        this.formData.password.length == 0
      ) {
        console.log("please complete the information");
        return;
      }
      this.$store.dispatch("blogLogin", this.formData);
    },
    toRegister() {
      this.$router.push({ path: "/register" });
    },
  },
};
</script>

<style scoped>
#login-page {
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.loginbox {
  padding: 10px;
  min-width: 30vw;
}
.loginbox .submit-box {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
/* .el-form-item__label {
  line-height: 500px;
  background: chartreuse;
} */
</style>
