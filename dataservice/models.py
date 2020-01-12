from django.db import models

# Create your models here.
class PotentialScamEmail(models.Model):
    email = models.CharField(max_length=50)
    designated_scam = models.BooleanField(default=False)
    number_encountered = models.IntegerField(default=0)
    first_updated = models.DateTimeField(auto_now_add=True)

class KnownScamEmails(models.Model):
    email = models.CharField(max_length=50)
    number_encountered = models.IntegerField(default=0)
    first_updated = models.DateTimeField(auto_now_add=True)


