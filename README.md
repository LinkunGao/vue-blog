# vue-blog

## frontend

- vuex
  https://vuex.vuejs.org/
  在依赖中安装 Vue.js devtools 到浏览器，并且在 main.js 的 vue object 上方添加 Vue.config.devtools = true;即可在浏览器中使用 vue 开发工具实时查看虚拟 dom，和 vuex 的值
  vue 的所有 axios 请求应该要写在 store.js 文件下的 action 函数中，在需要调用的组件中通过 this.$store.despatch('函数名'，parameters)实现
  ![avatar](/frontend/public/image_bug/vuex_life.jpg)
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

- .env 开始变量名为 VUE_APP_xxx

- 前端向后端 Django 发送 axios 请求时，直接发送字典对象，在后端是接收不了的
  - 安装 Qs, 将 Qs 导入当前组件，import Qs from "qs"; 并使用 Qs.stringify()方法将字典对象重新封装

## backend

- 安装 Django rest framework
  https://www.django-rest-framework.org/#installation
  pip install djangorestframework
  pip install markdown
  pip install django-filter

- Cors 跨源请求的安装：
  https://pypi.org/project/django-cors-headers/
  pip install django-cors-headers
  并将'corsheaders.middleware.CorsMiddleware', 写在 settings.py 文件中 middleware 中 common middleware 的上方
  在 settings.py 文件中配置跨域请求
  CORS_ALLOW_CREDENTIALS = True
  CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
"https://example.com",
"https://sub.example.com",
"http://localhost",
"http://127.0.0.1",
]

CORS_ALLOW_METHODS = [
"DELETE",
"GET",
"OPTIONS",
"PATCH",
"POST",
"PUT",
]

CORS_ALLOW_HEADERS = [
"accept",
"accept-encoding",
"authorization",
"content-type",
"dnt",
"origin",
"user-agent",
"x-csrftoken",
"x-requested-with",
]

- 爬虫： 安装 beautiful soup4
  - 官方文档：https://beautiful-soup-4.readthedocs.io/en/latest/

## Database design

- UserInfo
- Articles
- Category
- Favorite
- Like
- PaymentOrder
