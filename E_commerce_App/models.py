from django.db import models

# Create your models here.
class Catogerymodel(models.Model):
    Catogery_name=models.CharField(max_length=220)
    Catogery_img=models.ImageField(upload_to='Catogery',default='')

    def __str__(self):
        return self.Catogery_name 
    
class sub_catogerymodel(models.Model):
    Catogery=models.ForeignKey(Catogerymodel,on_delete=models.CASCADE)
    sub_Catogery_name=models.CharField(max_length=220)
    sub_Catogery_img=models.ImageField(upload_to='Sub_Catogery',default='')

    def __str__(self):
        return self.sub_Catogery_name 
    
class Productmodel(models.Model):
    sub_catogery=models.ForeignKey(sub_catogerymodel,on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=2000)
    Product_price=models.IntegerField()
    Product_dec=models.TextField()
    img=models.ImageField(upload_to='Product',default='')

    def __str__(self):
        return self.Product_name

class Cartmodel(models.Model):
    userID=models.IntegerField()
    productID=models.IntegerField()
    orderID=models.IntegerField(default=0)
    productname=models.CharField(max_length=220)
    productprice=models.IntegerField()
    productimage=models.ImageField(upload_to='Cartimage',default='')
    Quantity = models.IntegerField(default=2)

    def __str__(self):
        return self.productname

class Shipingmodel(models.Model):
    # orderId = models.IntegerField()
    userId = models.IntegerField()
    username =models.CharField(max_length=200)
    userEmail =models.EmailField()
    usercontect =models.IntegerField()
    Address = models.TextField()
    Area = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Pincode = models.BigIntegerField()
    Payment_Type = models.CharField(max_length=20)
    Date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk)

class faviourate_model(models.Model):
    userId = models.IntegerField()
    productID=models.IntegerField()
    pro_name = models.CharField(max_length=220)
    pro_img = models.ImageField( upload_to='fav')
    pro_dec = models.CharField(max_length=220)
    pro_price = models.IntegerField()

    def __str__(self) :
        return self.pro_name