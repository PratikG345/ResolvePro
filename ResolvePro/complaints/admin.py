from django.contrib import admin

# Register your models here.
from .models import Client,Job,Category,Resident

admin.site.register(Resident)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Job)