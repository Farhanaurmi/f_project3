from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request,'app/home.html')


def driver(request):
    drivers=Driver.objects.all()
    return render(request,'app/driver.html' , {'drivers':drivers})

def vehicle(request):
    vehicles=Vehicle.objects.all()
    return render(request,'app/vehicle.html' , {'vehicles':vehicles})


def bookinghistory(request):
    bookinghistorys=BookingHistory.objects.all()
    return render(request,'app/bookinghistory.html' , {'bookinghistorys':bookinghistorys})


def bookingdetails(request):
    bookingdetailss=BookingDetails.objects.all()
    return render(request,'app/bookingdetails.html' , {'bookingdetailss':bookingdetailss})

def customeruser(request):
    customerusers=CustomerUser.objects.all()
    return render(request,'app/customeruser.html' , {'customerusers':customerusers})