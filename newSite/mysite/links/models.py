from __future__ import unicode_literals
from django.db import models

class Links(models.Model):
    title = models.CharField(max_length=140)
    adresse = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
