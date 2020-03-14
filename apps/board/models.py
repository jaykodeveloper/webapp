from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(blank=False)
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to='static/time_line_photo/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Title: " + self.title

    class Meta:
        ordering = ['-created']