from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=555)

    def __str__(self):
        return self.name