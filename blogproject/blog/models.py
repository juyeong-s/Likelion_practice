from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    hits = models.IntegerField(default=0)

    def click(self):
        self.hits +=1
        self.save()
        
    def init(self):
        self.hits = 0
        self.save()