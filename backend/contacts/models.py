from django.core.validators import RegexValidator
from django.db import models


class Contact(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    message = models.TextField(max_length=1000)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.email
