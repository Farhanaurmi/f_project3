from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *



@unauthenticated_user
def loginuser(request):
    if request.method=='GET':
        return render(request,'app/loginuser.html', {'form':AuthenticationForm(),'form2':CreateUserForm()})
    else:
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'app/loginuser.html', {'form':AuthenticationForm(),'error':'Enter Correct Info','form2':CreateUserForm()})
        else:
            login(request,user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

@unauthenticated_user
def signupuser(request):

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
            
			admin = form.save()
			username = form.cleaned_data.get('username')

			Admin.objects.create(
				admin=admin,
				name=request.POST.get('name'),
                email=admin.email,
                contact_no=request.POST.get('contact_no'),
				)
			admin.save()
			login(request,admin)
			return redirect('home')			
	return redirect('loginuser')



@login_required
def home(request):
    return render(request,'app/home.html')

@login_required
def driver(request):
    if 'q' in request.GET:
        q=request.GET['q']
        drivers=Driver.objects.filter(driver_name__icontains=q)
    else:
        drivers=Driver.objects.all()
    return render(request,'app/driver.html' , {'drivers':drivers})

@login_required
@manager_only
def vehicle(request):
    if 'q' in request.GET:
        q=request.GET['q']
        vehicles=Vehicle.objects.filter(brand__icontains=q)
    else:
        vehicles=Vehicle.objects.all()
    return render(request,'app/vehicle.html' , {'vehicles':vehicles})

@login_required
@manager_only
def bookinghistory(request):
    if 'q' in request.GET:
        q=request.GET['q']
        bookinghistorys=BookingHistory.objects.filter(trip_type__icontains=q)
    else:
        bookinghistorys=BookingHistory.objects.all()
    return render(request,'app/bookinghistory.html' , {'bookinghistorys':bookinghistorys})

@login_required
@manager_only
def bookingdetails(request):
    bookingdetailss=BookingDetails.objects.all()
    return render(request,'app/bookingdetails.html' , {'bookingdetailss':bookingdetailss})

@login_required
@manager_only
def customeruser(request):
    if 'q' in request.GET:
        q=request.GET['q']
        customerusers=CustomerUser.objects.filter(user_name__icontains=q)
    else:
        customerusers=CustomerUser.objects.all()
    return render(request,'app/customeruser.html' , {'customerusers':customerusers})

@login_required
@manager_only
def alluser(request):
    admin = Admin.objects.all()
    return render(request,'app/alluser.html',{'admin':admin})

@login_required
@manager_only
def editdriver(request, pk):
    driver = Driver.objects.get(driver_id=pk)
    form = DriverFrom(instance=driver)
    if request.method == 'POST':
        form = DriverFrom(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver')
    return render(request,'app/editdriver.html', {'form':form})

@login_required
@manager_only
def edituser(request, pk):
    customeruser = CustomerUser.objects.get(User_Id=pk)
    form = CustomerUserFrom(instance=customeruser)
    if request.method == 'POST':
        form = CustomerUserFrom(request.POST, instance=customeruser)
        if form.is_valid():
            form.save()
            return redirect('customeruser')
    return render(request,'app/edituser.html', {'form':form})

@login_required
@manager_only
def deletedriver(request, pk):
	driver = Driver.objects.get(driver_id=pk)
	if request.method == "GET":
		driver.delete()
		return redirect('driver')

@login_required
@manager_only
def createdriver(request):
    form = DriverFrom()
    if request.method == 'POST':
        form = DriverFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver')
    return render(request,'app/createdriver.html', {'form':form})



@login_required
@manager_only
def createvehicle(request):
    if request.method == 'GET':
        return render(request, 'app/createvehicle.html', {'form':VehicleFrom()})
    else:
        try:
            vehicle = VehicleFrom(data=request.POST,files=request.FILES)
            vehicles = vehicle.save(commit=False)
            vehicles.user = request.user
            vehicles.save()
            return redirect('vehicle')
        except ValueError:
            return render(request, 'app/createvehicle.html', {'form':VehicleFrom()})


def notification(request):
    noti=Notification.objects.all()
    return render(request,'app/notification.html', {'noti':noti})


@login_required
@manager_only
def createnotification(request):
    form = NotificationFrom()
    if request.method == 'POST':
        form = NotificationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification')
    return render(request,'app/createnotification.html', {'form':form})

@login_required
@manager_only
def deletenotification(request,pk):
    obj=get_object_or_404(Notification,id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('notification')

@login_required
@manager_only
def coupons(request):
    coup=Coupons.objects.all()
    return render(request,'app/coupons.html', {'coup':coup})


@login_required
@manager_only
def createcoupons(request):
    form = CouponsFrom()
    if request.method == 'POST':
        form = CouponsFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coupons')
    return render(request,'app/createcoupons.html', {'form':form})

@login_required
@manager_only
def deletecoupons(request,pk):
    obj=get_object_or_404(Coupons,id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('coupons')

@login_required
@manager_only
def deletebookinghistory(request,pk):
    obj=get_object_or_404(BookingHistory,booking_history_id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('bookinghistory')

@login_required
@manager_only
def deletevehicle(request,pk):
    obj=get_object_or_404(Vehicle,vehicle_id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('vehicle')

@login_required
@manager_only
def deletebookingdetails(request,pk):
    obj=get_object_or_404(BookingDetails,booking_id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('bookingdetails')

@login_required
@manager_only
def deletecustomer(request,pk):
    obj=get_object_or_404(CustomerUser,User_Id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('customeruser')

