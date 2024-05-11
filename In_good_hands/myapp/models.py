from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField()


class Institution(models.Model):
    name = models.CharField()
    description = models.TextField()
    types = (
        (1, "fundacja"),
        (2, "organizacja pozarządowa"),
        (3, "zbiórka lokalna"),
        (4, "domyślnie fundacja")
    )
    type = models.IntegerField(choices=types)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField()
    phone_number = models.CharField()
    city = models.CharField()
    zip_code = models.CharField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
