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
              <!-- <div>{{ article_info.title }}</div> -->
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
              v-if="img == cover_img"
              class="cover"
              style="width: 150px; height: 150px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
            <el-image
              v-else
              style="width: 150px; height: 150px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
          </div>
          <el-button @click="submitArticle" type="success" round
            >Save</el-button
          >
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
import axios from "axios";
export default {
  data() {
    return {
      article_info: {
        title: "",
        describe: "",
        contents: "",
      },
      // 存储用户选择的封面图片
      cover_img: "",
      // 存储所有用户上传的预览图片
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
            self.article_info.contents = contents;
          },
          // 本地图片上传
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
          // 远程图片添加
          onImageLinkInsert(url) {
            let imgNode = document.createElement("img");
            imgNode.src = url;
            $("#summernote").summernote("insertNode", imgNode);
            self.cover_list.push(url);
          },
          // 监听删除媒体文件
          onMediaDelete(target) {
            console.log(target);
            let imgData = target[0].src;
            for (let index = 0; index < self.cover_list.length; index++) {
              if (self.cover_list[index] == imgData) {
                self.cover_list.splice(index, 1);
              }
            }
          },
        },
      });
    },
    // 选择封面
    chooseCover(img) {
      this.cover_img = img;
    },
    // 提交到后端
    submitArticle() {
      let article_data = {
        title: this.article_info.title,
        describe: this.article_info.describe,
        content: this.article_info.contents,
        cover: this.cover_img,
      };
      // console.log(process.env);
      // console.log(process.env.VUE_APP_BASE_URL);
      axios
        .post(process.env.VUE_APP_BASE_URL + "add-article/", article_data)
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.error(err);
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
.dweb .el-image:hover {
  border: 2px solid #ffc815;
}
.dweb .el-image.cover {
  border: 2px solid #ffc815;
}
.dweb .el-image {
  margin: 1px;
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
