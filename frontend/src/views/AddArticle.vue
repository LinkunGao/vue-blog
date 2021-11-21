<template>
  <div id="add-article">
    <el-row :gutter="10">
      <el-col :xs="24" :lg="8">
        <div class="dweb">
          <el-form
            :label-position="'left'"
            label-width="100px"
            :model="article_info"
          >
            <el-form-item label="Article Title">
              <el-input v-model="article_info.title"></el-input>
            </el-form-item>
            <el-form-item label="Description">
              <el-input
                type="textarea"
                v-model="article_info.describe"
                :rows="4"
              ></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
      <el-col :xs="24" :lg="16">
        <div class="dweb">
          <div v-for="(img, index) in cover_list" :key="index">
            <el-image
              style="width: 100px; height: 100px"
              :src="img"
              :fit="'cover'"
            ></el-image>
          </div>
          <el-button type="success" round>Save</el-button>
        </div>
      </el-col>
      <el-col :xs="24" :lg="24">
        <div class="dweb">
          <div id="summernote"></div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import $ from "jquery";
export default {
  data() {
    return {
      article_info: {
        title: "",
        describe: "",
      },
      cover_list: [],
    };
  },
  mounted() {
    // 在最后一次刷新页面之前，调用函数
    this.summernote();
  },
  methods: {
    // 对富文本框的操作
    summernote() {
      // 进入子函数先保存当前函数的this，以避免与之后的重复报错
      let self = this;
      $("#summernote").summernote({
        width: "100%",
        height: 300,
        lang: "zh-CN",
        callbacks: {
          // 当输入时
          onChange(contents) {
            console.log(contents);
          },
          onImageUpload(files) {
            // console.log(files);
            let img = files[0];
            let imgData = new FileReader();
            imgData.readAsDataURL(img);
            // console.log(imgData);
            imgData.onload = function () {
              // 插入图片到富文本框中
              let imgNode = document.createElement("img");
              imgNode.src = imgData.result;
              // 获取富文本框，并将创建的img插入进去
              $("#summernote").summernote("insertNode", imgNode);
              // 将上传的图片推入cover_list中展示，待选择
              self.cover_list.push(imgData.result);
            };
          },
        },
      });
    },
  },
};
</script>

<style scoped>
/* 当写了scoped 表明该css样式只作用于当前的组件 */
.dweb {
  /* height: 200px; */
  min-height: 200px;
  padding: 20px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-form-item {
  margin-top: 22px;
}
.dweb .el-button {
  position: fixed;
  right: 20px;
  margin-top: 255px;
  z-index: 1001;
}
</style>
