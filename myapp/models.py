from django.db import models

#models down here

class Boodschappen(models.Model):
    Product_1 = models.CharField(max_length=200)
    Product_2 = models.CharField(max_length=200)


    def __str__(self):
        return self.Product_1 + '' + self.Product_2