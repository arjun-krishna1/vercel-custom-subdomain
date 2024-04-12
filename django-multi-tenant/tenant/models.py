from django.db import models

class Tenant(models.Model):
    nickname = models.CharField(max_length=255)
    backstory = models.CharField(max_length=255)
