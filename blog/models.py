from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # passing default function as actual value as timezone.now not as timezone.now()
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user is deleted then post is also deleted by using on_delete=models.CASCADE
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
