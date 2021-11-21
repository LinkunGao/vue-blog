from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog_backend.models import Articles 
# 导入爬虫包
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import base64
import requests
import datetime

hostUrl = 'http://127.0.0.1:9000/'

@api_view(['POST'])
def add_article(request):
    title = request.POST['title']
    describe = request.POST['describe']
    cover = request.POST['cover']
    content = request.POST['content']

    # 保存文章
    new_article = Articles(title=title)
    new_article.save()

    # 利用爬虫工具解析富文本文档
    soup = BeautifulSoup(content, 'html.parser')
    # 获取所有img标签 图片
    imgList = soup.find_all('img')
    
    for index in range(0,len(imgList)):
        # print(type(imgList[index]))
        # 获取每个img标签下的src属性， 以便之后下载
        # print(imgList[index]['src'])
        src = imgList[index]['src']
        # 判断是远程还是本地？
        if 'http://' in src or  'https://' in src:
            # 请求远程图片
            image = requests.get(src)
            # 将图片转化为二进制才能打开
            image_data = Image.open(BytesIO(image.content))
            # 设定唯一的文件名
            # image_name = 时间 + 文章id + 图片位标
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+ str(new_article.id)+'-'+str(index)
            image_data.save('upload/'+image_name+'.png')
            new_src = hostUrl + 'upload/'+image_name+'.png'
            content = content.replace(src, new_src)
            # set up cover
            if cover == src:
                cover = new_src
        else:
            # 保存本地上传图片
            image_data = base64.b64decode(src.split(',')[1])
            image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'-'+ str(new_article.id)+'-'+str(index)+'.'+src.split(',')[0].split('/')[1].split(';')[0]
            # print(image_name)
            image_url = os.path.join('upload',image_name).replace('\\','/')
            with open(image_url,'wb') as f:
                f.write(image_data)
            new_src = hostUrl + image_url
            content = content.replace(src, new_src)
            # set up cover
            if cover == src:
                cover = new_src

    new_article.describe = describe 
    new_article.content = content
    new_article.cover = cover
    
    new_article.save()     


    return Response('ok')