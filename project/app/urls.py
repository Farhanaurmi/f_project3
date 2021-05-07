from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('driver', views.driver),
    path('vehicle', views.vehicle),
    path('bookinghistory', views.bookinghistory),
    path('bookingdetails', views.bookingdetails),
    path('customeruser', views.customeruser),

]