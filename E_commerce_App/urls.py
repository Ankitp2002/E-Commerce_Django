from django.urls import path
from .views import *    

urlpatterns = [

    path("",Catogeryviews,name='Catogery'),
    path("sub_cat/<int:subCatId>",SubCatogeryviews,name='sub_Catogery'),
    path('pro/<int:procatId>',productviews,name='Product'),
    path('pro_all/',proallview,name='proall'),
    path('pro_detail/',prodetails,name='prodetails'),
    path('cart/',Cartview,name='Carturl'),
    path('shiping/',shipingview,name='shipingurl'),
    path('orderlist/',orderlistview,name='orderlisturl'),
    path('orderdetail/',orderdetaisview,name='orderdetailurl'),
    path('search/',searchview,name='searchurl'),
    path('faviourate/',faviouratview,name='faviourateurl'),
    path('cartjs/',cartjsview,name='carjsurl'),
]