from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
