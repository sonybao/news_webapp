from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(null=True, blank=True, upload_to="profiles.images/")
    media_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.user)