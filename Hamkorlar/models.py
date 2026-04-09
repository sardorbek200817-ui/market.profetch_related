from django.db import models
from ombor.models import Product

PARTNER_TYPE = [
    ('T' ,"Taminotchi"),
    ("M" , 'Mijoz')
]


class Partner(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=30)
    type = models.CharField(choices=PARTNER_TYPE)
    def __str__(self):
        return self.name

        
class Product_in(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.CASCADE , related_name='product_in')
    reciever = models.ForeignKey(Partner,on_delete=models.CASCADE , related_name='recievers')
    amount = models.PositiveBigIntegerField()
    price = models.FloatField()
    data = models.DateField() 
    def __str__(self):
        return f"{self.product}"



class Product_out(models.Model):
    customer = models.ForeignKey(Partner , on_delete=models.CASCADE,
    related_name='customers')
    product = models.ManyToManyField(Product , related_name='product_out')
    summa = models.FloatField()
    data = models.DateField()
    amout = models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.product}"
    


# related_name = 'product_out' bu shu modelning nameni
# bu yerda biz Product uchun qaysi modeldagi malumotlarni olishni related_name orqali ishlatamiz

    

    

































