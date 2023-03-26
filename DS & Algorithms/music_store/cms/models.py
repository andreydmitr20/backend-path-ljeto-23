from django.db import models


class Service(models.Model):
    """A service"""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.URLField(default="", blank=True)
    price = models.IntegerField(default=0, blank=True)
