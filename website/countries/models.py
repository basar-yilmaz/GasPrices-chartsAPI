from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    lpg_locale = models.CharField(max_length=20, blank=False, null=False)
    lpg_euro = models.CharField(max_length=20, blank=False, null=False)
    diesel_locale = models.CharField(max_length=20, blank=False, null=False)
    diesel_euro = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name
