from django.db import models

# Create your models here.
class Item(models.Model):
    imageId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    gender = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    monthlySales = models.IntegerField()
    oily_point = models.IntegerField()
    dry_point = models.IntegerField() 
    sensitive_point = models.IntegerField() 

    def __str__(self):
        return self.name
    