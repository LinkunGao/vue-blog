<template>
  <div id="app">
    <!-- 头部导航 -->
    <div id="top-menu" class="dweb"></div>
    <!-- 侧边栏 -->
    <div id="left-menu" :class="'dweb ' + mobile_left">
      <i @click="showHideLeftMenu" id="left-btn" class="el-icon-menu"></i>
    </div>
    <!-- 网页内容 -->
    <div id="content" :class="mobile_content">
      <el-row :gutter="20">
        <!-- 多行选择，复制要更改的文字，command+d -->
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
      </el-row>

      <el-row :gutter="20">
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
      </el-row>

      <el-row :gutter="20">
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
      </el-row>

      <el-row :gutter="20">
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
        <el-col :xs="24" :lg="8"
          ><div class="dweb" style="height: 200px"></div
        ></el-col>
      </el-row>

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
    window.onresize = () => {
      this.screenWidth = document.body.clientWidth;
    };
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
  },
};
</script>

<style>
.el-col {
  margin-top: 5px;
}
</style>
