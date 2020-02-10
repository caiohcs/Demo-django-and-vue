from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    logo = models.CharField(max_length=1000)
    inserted_at = models.DateTimeField(auto_now_add=True)
    used_on_this_page = models.BooleanField()
