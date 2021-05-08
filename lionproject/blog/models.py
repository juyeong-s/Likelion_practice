from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self): #목록에 Blog Object말고 글의 제목이 뜨도록 함.
        return self.title

    def summary(self):
        return self.body[:100] #100번째 인덱스까지 잘라서 보여줌