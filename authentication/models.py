from asyncio.windows_events import NULL
from email.policy import default
from ssl import _PasswordType
from django.db import models

# Create your models here.
class Authentication(models.Model):
    first_name = models.CharField(max=20,NULL=True)
    last_name = models.CharField(max=20,NULL=True)
    email = models.models.EmailField(("@"), max_length=254)
    phoneNumber = models.PhoneNumberField(max=20, NULL=True)
    Password = models.CharField(max=20,NULL=True)
    