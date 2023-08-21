from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name=("Username")) 
    email = models.EmailField(unique=True, verbose_name=("Email Address"))
    favorite_animal = models.CharField(max_length=255, verbose_name=("Favorite Animal"))
    pass