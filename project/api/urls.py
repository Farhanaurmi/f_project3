from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('driver', views.DriverList.as_view()), 
    path('customeruser', views.CustomerUserList.as_view()),
    path('vehicle', views.VehicleList.as_view()),
    path('bookingdetails', views.BookingDetailsList.as_view()),
    path('bookinghistory', views.BookingHistoryList.as_view()),
    path('notification', views.notificationList.as_view()),
    path('coupons', views.CouponsList.as_view()),
    path('contact', views.contactList.as_view()),
]
