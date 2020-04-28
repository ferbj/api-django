from django.db import models
# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    countryisocode = models.CharField(max_length=5)
    date = models.CharField(max_length=4)
    quantity = models.FloatField()

    def NameCountry(self):
        cadena = "Pais : {0} , Cantidad: {1}"
        return cadena.format(self.name, self.quantity)

    def __str__(self):
        return self.NameCountry()
