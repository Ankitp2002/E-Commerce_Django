from django.urls import path
from .views import *    
urlpatterns = [

    path("Register/",Registrationview,name='Register'),
    path("",Loginview,name='Login'),
    path('logout/',Logoutview,name='Logout'),
    path('profile/',profileview,name='profileurl'),
    path('about/',aboutview,name='abouturl'),

]