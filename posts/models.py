from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=80)
    select1_content = models.CharField(max_length=100)
    select2_content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_posts', blank=True)
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_posts', blank=True)