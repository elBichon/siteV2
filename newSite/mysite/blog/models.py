from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    cate = models.CharField(max_length=140)
    resume=models.TextField()
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

