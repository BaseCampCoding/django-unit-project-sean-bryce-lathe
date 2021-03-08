from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    about = models.TextField(max_length=2000)
    genre = models.CharField()
    image = models.ImageField()
    role = (
        ('Listener', "Listener"),
        ('Artist', "Artist")
    )
    roles = models.CharField(max_length=8,choices=role, default="Listener")