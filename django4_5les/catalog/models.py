from django.db import models


class Catalog(models.Model):
    name = models.CharField(verbose_name='name', max_length=128)
    price = models.DecimalField(verbose_name='price', max_digits=8,
                                decimal_places=0, default=0)
    weight = models.DecimalField(verbose_name='weight', max_digits=6,
                                decimal_places=0, default=0)
