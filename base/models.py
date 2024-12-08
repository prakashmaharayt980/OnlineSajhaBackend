from django.db import models
from django.utils import timezone
import uuid
class NewsData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    type_of_news = models.CharField(max_length=100)
    post_by = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    news = models.ForeignKey(NewsData, related_name='post_images', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    def __str__(self):
        return f"Image for {self.news.title if self.news else 'No News'}"


class AdsImage(models.Model):
    news = models.ForeignKey(NewsData, related_name='ads_images', on_delete=models.SET_NULL, null=True, blank=True,db_index=True)
    image = models.ImageField(upload_to='ads_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.news.title if self.news else 'No News'}"


class CreateAdsImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='CreateAdsSeperate/')  # Upload images to the 'post_images/' folder
    post_by = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)  # Automatically set the creation date

    def __str__(self):
        return self.title
