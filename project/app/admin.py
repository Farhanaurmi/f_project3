from django.contrib import admin
from .models import Driver,CustomerUser,Vehicle

admin.site.register((Driver,CustomerUser,Vehicle))
