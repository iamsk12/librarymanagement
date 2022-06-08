from django.db import models
from django.contrib.auth.models import User

#model for book
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    admin = models.ForeignKey(User,blank=True ,on_delete=models.CASCADE)
    class Meta:
        db_table = "book"

