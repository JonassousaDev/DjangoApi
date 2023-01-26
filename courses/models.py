from django.db import models

class Curse(models.Model):
    name = models.CharField(max_length=20)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
