from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ("admin", "админ"),
            ("moderator", "модератор"),
            ("user", "юзер"),
        ],
        default="user",
    )

    def __str__(self):
        return self.email
