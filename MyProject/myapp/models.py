from django.db import models
from users.models import User

class Clothes(models.Model):
    title = models.CharField(max_length=200)
    path = models.ImageField(upload_to="img/%Y/%m/%d/", blank=True)
    description = models.TextField()
    price =  models.DecimalField(max_digits = 5, decimal_places = 2) 
    quantity = models.IntegerField()

    def total_likes(self):
        return Like.objects.filter(clothes=self).count()
    
    def total_comments(self):
        return Comment.objects.filter(clothes=self).count()

    def user_liked(self, user):
        return Like.objects.filter(clothes=self, user=user).exists()
    
    def user_comment(self, user):
        return Comment.objects.filter(clothes=self, user=user).exists()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'clothes')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user} on {self.clothes}'
    
class Cart(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
