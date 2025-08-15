from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    full_address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.user.username