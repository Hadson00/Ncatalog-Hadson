from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clothes(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    description = models.TextField()

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    clothes_id = models.ForeignKey(Clothes, on_delete=models.CASCADE)

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    roupa_id = models.ForeignKey(Like, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)