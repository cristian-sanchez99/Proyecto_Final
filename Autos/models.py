from tabnanny import verbose
from django.db import models

# Create your models here.
class Autos(models.Model):
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length= 150,blank = True, null = True)
    price = models.FloatField()
    SKU = models.CharField(max_length= 30, unique=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = "autos")
    
    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

class Motocicletas(models.Model):
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length= 150,blank = True, null = True)
    price = models.FloatField()
    SKU = models.CharField(max_length= 30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Motocicleta"
        verbose_name_plural = "Motocicletas"

class Camionetas(models.Model):
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length= 150,blank = True, null = True)
    price = models.FloatField()
    SKU = models.CharField(max_length= 30, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Camioneta"
        verbose_name_plural = "Camionetas"

    
