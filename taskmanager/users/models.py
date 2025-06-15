from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.user.username