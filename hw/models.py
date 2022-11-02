from django.db import models

from django.conf import settings


# class Human (models.Model):
#     name = models.CharField(max_length=250, blank=False)
#     surname = models.CharField(max_length=250,blank=False)
#     phone_number = models.CharField(max_length=12, blank=False)
#     passport_id = models.OneToOneField(
#     Passport,
#     blank=False,
#     on_delete=models.CASCADE,
#     primary_key=True,
#     blank=False,
#     # default = User.objects.first().id,
#     )
#     date_ofbirth = models.DateField(blank = True)

# class Passport (models.Model):
