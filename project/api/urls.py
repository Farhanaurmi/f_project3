from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('driver', views.DriverList.as_view()), 
    path('customeruser', views.CustomerUserList.as_view()),
    path('vehicle', views.VehicleList.as_view()),
    path('bookingdetails', views.BookingDetailsList.as_view()),
    path('bookinghistory', views.BookingHistoryList.as_view()),
]