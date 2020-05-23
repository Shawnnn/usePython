from django.db import models
from django.utils import timezone

# Create your models here.
# 创建一个博客文章模型

class Post(models.Model):  # models.Model 表明是Django模型，所以Django知道它应该被保存在数据库中
    author = models.ForeignKey('auth.User', on_delete= models.CASCADE) # models.ForeignKey 指向另一个模型的连接
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title




