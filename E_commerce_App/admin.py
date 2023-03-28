from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Catogerymodel)
class sub_catogeryadmin(admin.ModelAdmin):
    list_display = ['Catogery','sub_Catogery_name']
admin.site.register(sub_catogerymodel,sub_catogeryadmin)
class Productadmin(admin.ModelAdmin):
    list_display=['pk','sub_catogery','Product_name','Product_price']
admin.site.register(Productmodel,Productadmin)
class Cartadmin(admin.ModelAdmin):
    list_display = ['pk','userID','productID','orderID','productname']
admin.site.register(Cartmodel,Cartadmin)

class shipingadmin(admin.ModelAdmin):
    list_display =['userId','username','userEmail','usercontect','Address','City','Payment_Type']
admin.site.register(Shipingmodel,shipingadmin)
class faviourateadmin(admin.ModelAdmin):
    list_display = ["userId","pro_name","pro_img","pro_dec","pro_price"]
admin.site.register(faviourate_model,faviourateadmin)