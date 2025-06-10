from django.db import models

class Posts(models.Model):
    picture = models.ImageField(default="media/default.jpg" ,null=True, blank=True)
    caption = models.CharField(null=True, blank=True)