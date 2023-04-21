from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=80)
    select1_content = models.CharField(max_length=100)
    select1_image = models.ImageField(blank=True, upload_to='balance_game_images/%Y/%m/%d/')
    select2_content = models.CharField(max_length=100)
    select2_image = models.ImageField(blank=True, upload_to='balance_game_images/%Y/%m/%d/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_posts', blank=True)
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_posts', blank=True)