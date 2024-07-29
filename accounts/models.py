from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    cost_price = models.FloatField(null=True)
    selling_price = models.FloatField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField(null=True)
    selling_price = models.FloatField(null=True)
    sale_date = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def profit(self):
        return (self.selling_price - self.product.cost_price) * self.quantity_sold
        

    def __str__(self):
        return f"Sale of {self.quantity_sold} {self.product.name}(s) on {self.sale_date}"
    


