from django.contrib import admin
from .models import Driver,CustomerUser

admin.site.register((Driver,CustomerUser))
