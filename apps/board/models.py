from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(blank=False, max_length=255)
    body = models.TextField(blank=False)
    image = models.ImageField(upload_to='time_line_photo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created']