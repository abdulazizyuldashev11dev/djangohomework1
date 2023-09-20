from django.db import models

class NewsModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title