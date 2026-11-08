from django.db import models


class Phone(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_length=10, max_digits=10,decimal_places=3,default=0.000)
    image = models.URLField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)