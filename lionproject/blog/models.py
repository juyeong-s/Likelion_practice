from django.db import models


class Post(models.Model):  # Post 데이터베이스를 하나 만든거임
    title = models.CharField(max_length=100)
    content = models.TextField()
    image_1 = models.ImageField(blank=True, upload_to='blog') #빈 값이 True --> 사용자가 이미지를 안넣어도 된다는 것
    image_2 = models.ImageField(blank=True, upload_to='blog2')
    # media에 blog라는 폴더가 생성되고 거기에 사진이 저장된다는 뜻
    # image = models.ImageField(blank=True, upload_to='blog2') 를 하나 더 추가하면 사진 두개 받을 수 있고, blog2 폴더생성
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}' #내 자신의 title속성을 리턴

