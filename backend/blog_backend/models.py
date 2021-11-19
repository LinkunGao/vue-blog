from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# User infomation
class UserInfo(models.Model):
    icon = models.ImageField()
    nickName = models.CharField()
    # 一对一，用户个人信息表关联Django user 表
    belong_to = models.OneToOneField(User)
    def __int__(self):
        return self.id

# Articles information
class Articles(models.Model):
    title = models.CharField()
    cover = models.CharField()
    text = models.TextField()
    # 多对一，这些文章属于哪个用户
    belong_to = models.ForeignKey(UserInfo)
    def __int__(self):
        return self.id

class Category(models.Model):
    name = models.CharField()
    # 递归设计，根目录是没有foreign key的，任何一个节点都可以查询自身旗下的子节点
    belong = models.ForeignKey(self)
    def __int__(self):
        return self.id
# 收藏
class Favorite(models.Model):
    belong_user = models.ForeignKey(UserInfo)
    belong_article = models.ForeignKey(Articles)
    def __int__(self):
        return self.id

# 点赞
class Like(models.Model):
    belong_article = models.ForeignKey(Articles)
    belong_user = models.ForeignKey(UserInfo)
    total_num = models.IntegerField()
    def __int__(self):
        return self.id

# 打赏
class PaymentOrder(models.Model):
    order = models.CharField()
    price = models.CharField()
    status = models.BooleanField()
    def __int__(self):
        return self.id