from django.db import models

# Create your models here.
class Toppings(models.Model):
    nombre = models.CharField(max_length=35)
    precio = models.DecimalField(max_digits=4,null=True, blank=True, default=00.00, decimal_places=2)

    def _str_(self):
        return f"(self.nombre)"
