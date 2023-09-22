from django.db import models
from mysite import settings


class NewsModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=2)
    def __str__(self):
        return self.title