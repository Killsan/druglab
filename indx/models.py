from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_cost = models.CharField(max_length=10)
    product_description = models.CharField(max_length=1000)
    product_img = models.ImageField(upload_to='indx/images/')

    def __str__(self):
        return self.product_name