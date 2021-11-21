<template>
  <div id="app">
    <!-- 头部导航 -->
    <div id="top-menu" class="dweb"></div>
    <!-- 侧边栏 -->
    <div id="left-menu" :class="'dweb ' + mobile_left">
      <i @click="showHideLeftMenu" id="left-btn" class="el-icon-menu"></i>
      <!-- 导航栏 -->
      <el-col :span="24" style="margin-top: 80px">
        <!-- 导航栏路由跳转方案二： @select="chooseMenu" -->
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#00000000"
          text-color="#fff"
          active-text-color="#ffd04b"
          router
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-folder-opened"></i>
              <span>Articles Management</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/add-article">Publish Ariticle</el-menu-item>
              <el-menu-item index="1-2">Article List</el-menu-item>
              <!-- <el-menu-item index="1-3">选项3</el-menu-item> -->
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="2">
            <i class="el-icon-user"></i>
            <span slot="title">User Management</span>
          </el-menu-item>
          <el-menu-item index="3">
            <i class="el-icon-coin"></i>
            <span slot="title">Reward History</span>
          </el-menu-item>
          <el-menu-item index="4">
            <i class="el-icon-s-operation"></i>
            <span slot="title">Section Management</span>
          </el-menu-item>
          <el-menu-item index="/logout">
            <i class="el-icon-back"></i>
            <span slot="title">Logout</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
    <!-- 网页内容 -->
    <div id="content" :class="mobile_content">
      <router-view></router-view>

      <div id="footer" class="dweb">
        <span> Copyright Ⓒ 2021 SkyCoco </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      screenWidth: document.body.clientWidth,
      mobile_left: "",
      mobile_content: "",
    };
  },
  mounted() {
    // 监听页面变化，对当前屏幕宽度重新赋值
    // window.onresize = () => {
    //   this.screenWidth = document.body.clientWidth;
    // };
    this.changeDevice();
  },
  methods: {
    // 当屏幕变化时，改变布局
    changeDevice() {
      if (this.screenWidth <= 500) {
        this.mobile_left = "xs";
        this.mobile_content = "xs";
      } else {
        this.mobile_left = "";
        this.mobile_content = "";
      }
    },
    showHideLeftMenu() {
      if (this.mobile_left == "") {
        this.mobile_left = "xs";
      } else {
        this.mobile_left = "";
      }
      // 宽屏状态下
      if (this.screenWidth > 500) {
        if (this.mobile_content == "") {
          this.mobile_content = "xs";
        } else {
          this.mobile_content = "";
        }
      }
    },
    // 跳转到添加文章页面
    // chooseMenu(index) {
    //   // element ui 导航栏页面跳转方法二，不使用自带的router方案
    //   this.$router.push({ path: index });
    // },
  },
};
</script>

<style>
.el-col {
  margin-top: 5px;
}
</style>
