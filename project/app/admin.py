from django.contrib import admin
from .models import *

admin.site.register((Driver,CustomerUser,Vehicle,BookingHistory,BookingDetails,Admin,Notification,Coupons,Brand,BrandModel,Insurance,Frompoint,Contact))
