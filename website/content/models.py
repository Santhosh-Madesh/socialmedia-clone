from django.db import models

class Posts(models.Model):
    picture = models.ImageField(default="media/default.jpg" ,null=True, blank=True)
    caption = models.CharField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)

class Comments(models.Model):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(null=True, blank=True)