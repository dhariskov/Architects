from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()
# Create your models here.
class Profile(models.Model):
    display_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

