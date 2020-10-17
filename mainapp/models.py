from django.db import models

class Color(models.Model):
    color_name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    depth = models.IntegerField()
    colours = models.ManyToManyField(Color)
    material = models.CharField(max_length=100)
    image = models.CharField(max_length=500)