<template>
  <div id="register-page">
    <div class="dweb registerbox">
      <div class="header">
        New User Sign Up
        <el-divider></el-divider>
      </div>
      <el-form :label-position="'right'" label-width="135px" :model="formData">
        <el-form-item label="Username">
          <el-input v-model="formData.username"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="formData.password" type="password"></el-input>
        </el-form-item>
        <el-form-item label="Comfirm Password">
          <el-input
            v-model="formData.confirm_password"
            type="password"
          ></el-input>
        </el-form-item>
        <el-form-item class="submit-box">
          <el-button @click="blogRegister()" type="success">Comfirm</el-button>
          <el-button @click="toLogin()" type="warning"
            >Already have an account</el-button
          >
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
        confirm_password: "",
      },
    };
  },
  methods: {
    toLogin() {
      this.$router.push({ path: "/login" });
    },
    blogRegister() {
      if (
        !!this.formData.username &&
        !!this.formData.password &&
        !!this.formData.confirm_password
      ) {
        if (this.formData.password != this.formData.confirm_password) {
          alert("The password should be same!");
          return;
        }
        if (this.formData.password.length < 8) {
          alert("The password too short!");
          return;
        }
        this.$store.dispatch("blogRegister", this.formData);
      } else {
        alert("Please complete the form");
        return;
      }
    },
  },
};
</script>

<style scoped>
#register-page {
  height: 80vh;
  /* width: 65vw; */
  display: flex;
  align-items: center;
  justify-content: center;
}
.registerbox {
  padding: 10px;
  min-width: 30vw;
}
</style>
