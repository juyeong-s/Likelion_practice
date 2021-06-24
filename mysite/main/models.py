from django.db import models
from django.conf import settings
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}' #내 자신의 title속성을 리턴

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.post}' 