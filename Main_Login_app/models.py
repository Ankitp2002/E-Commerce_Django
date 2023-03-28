from django.db import models

# Create your models here.
class Registermodal(models.Model):
    Name=models.CharField(max_length=110)
    Mo_No=models.BigIntegerField()
    Email=models.EmailField()
    Password=models.BigIntegerField()
    image =models.ImageField(upload_to='Profile_img',default='')
    
    def __str__(self):
        return self.Name