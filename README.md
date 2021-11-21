# vue-blog

## frontend

- 安装 element UI:
  https://element.eleme.io/#/en-US
- 富文本（jquery and bootstrap 的 webpack 引入）summernote
  https://summernote.org/getting-started/
  - 在 vue 开发依赖环境下安装 jquery, bootstrap(以及旗下的 popper.js 和 npm i @popperjs/core), summernote
  - 固定版本安装：
    "jquery": "3.5.1", npm install --save-dev jquery@3.5.1
    "popper.js": "1.16.1",
    "bootstrap": "4.5.0",
    "summernote": "0.8.18", 固定版本号，必须把"jquery": "^3.5.1"的^小箭头删掉
    ![avatar](/frontend/public/image_bug/summernote.png)

## Database design

- UserInfo
- Articles
- Category
- Favorite
- Like
- PaymentOrder
