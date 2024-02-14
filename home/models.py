from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "user"

class Books(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)

    class Meta:
        db_table = "book"