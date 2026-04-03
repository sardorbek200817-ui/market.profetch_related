1 ]  <!-- https://admin.ecoart.uz/dashboard/warehouse/products -->

bizning product uchun misol tariqasi korsatilgan

2 ] category = models.ManyToManyField(to="Category" , related_name="products")
    to='Category' bu qaysi Category modeliga boglanishini belgilaydi

ManyToMany qoydasi >>>>>  Bitta Product > bir nechta Category
Bitta Category > bir nechta Product







class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='products/img' , blank=True , null=True)
    category = models.ManyToManyField(to="Category" , related_name="products")
    unit = models.CharField( UNITS,default='piece')
    amout = models.IntegerField()



class Category(models.Model):
    name = models.CharField(max_length=30)


bu yerdas agarda     category = models.ManyToManyField(to="Category" , related_name="products")
ManyToManyField orniga Foreinkey bolganda   Product ni boshqa modellarga ulab bolmas edi ManyToMany shu modelni ham boshqa joylarda ishlashiga yordam beradi
