from django.urls import path
from .views import *    
urlpatterns = [
    path('',socialview,name='E_app'),
    path('profile/',profile_view,name='Profile_url')
]