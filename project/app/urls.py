from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driver', views.driver, name='driver'),
    path('createdriver', views.createdriver, name='createdriver'),
    path('driver/<int:pk>/delete', views.deletedriver, name='deletedriver'),
    path('editdriver/<int:pk>', views.editdriver, name='editdriver'),
    path('edituser/<int:pk>', views.edituser, name='edituser'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('createvehicle', views.createvehicle, name='createvehicle'),
    path('bookinghistory', views.bookinghistory),
    path('bookingdetails', views.bookingdetails),
    path('customeruser', views.customeruser, name='customeruser'),
    path('users', views.alluser),
    path('signup', views.signupuser, name='signupuser'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),

]