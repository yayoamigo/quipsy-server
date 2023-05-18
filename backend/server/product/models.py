from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_discount(self):
        return float(self.price) * 0.5
        