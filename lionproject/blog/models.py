from django.db import models


class Post(models.Model):  # Post 데이터베이스를 하나 만든거임
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}' #내 자신의 title속성을 리턴