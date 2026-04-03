from django.db import models

UNITS = [
    ('l' , 'Litr'),
    ('piece' , 'Dona'),
    ('box' , 'Quti'),

]

class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='products/img' , blank=True , null=True)
    category = models.ManyToManyField(to="Category" , related_name="products")
    unit = models.CharField( UNITS,default='piece')
    amout = models.IntegerField()
    
    def __str__(self):
        return self.name
    



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



































