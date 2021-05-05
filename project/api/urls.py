from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('driver', views.DriverList.as_view()), 
    path('customeruser', views.CustomerUserList.as_view()),
]