from django.contrib import admin
from .models import *
# Register your models here.
class regisdteradmin(admin.ModelAdmin):
    list_display = ['Name','Mo_No','Email','Password']
admin.site.register(Registermodal)