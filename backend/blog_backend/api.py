from rest_framework.response import Response
from rest_framework.decorators import api_view
# 导入爬虫包
from bs4 import BeautifulSoup
import requests

@api_view(['POST'])
def add_article(request):
    title = request.POST['title']
    describe = request.POST['describe']
    cover = request.POST['cover']
    content = request.POST['content']
    
    # 利用爬虫工具解析富文本文档
    soup = BeautifulSoup(content, 'html.parser')
    # 获取所有img标签 图片
    imgList = soup.find_all('img')
    
    for index in range(0,len(imgList)):
        # print(type(imgList[index]))
        # 获取每个img标签下的src属性， 以便之后下载
        print(imgList[index]['src'])


    return Response('ok')