from django.db import models
from django.conf import settings

# Create your models here.

class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    preview = models.CharField(max_length=250)
    full_view = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='news_images', null=True, blank=True)
    
    def __str__(self):
        return f"{settings.MEDIA_URL}{self.image}"