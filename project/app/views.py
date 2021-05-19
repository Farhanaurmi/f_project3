from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *
from django.db.models import Q
import datetime
from django.utils.crypto import get_random_string
from .filters import *


######LOGIN & REGISTER#######

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


##########HOME############

@login_required
def home(request):
    driver=Driver.objects.all().filter(status='UNDER VARIFICATION').count()
    booking_req= BookingDetails.objects.all().filter(assign_driver=None).filter(reject=False).count()
    return render(request,'app/home.html',{'driver':driver,'booking_req':booking_req})


#######ALL THE PAGE FUNCTIONALITY########

@login_required
@manager_only
def driver(request):
    if 'q' in request.GET:
        q=request.GET['q']
        drivers=Driver.objects.filter(driver_name__icontains=q)
        drivers = drivers.filter(Q(status='ACTIVE') | Q(status='OFFLINE') | Q(status='ON A RIDE'))
    else:
        drivers=Driver.objects.all().filter(Q(status='ACTIVE') | Q(status='OFFLINE') | Q(status='ON A RIDE'))
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
        bookingdetailss=BookingDetails.objects.filter(booking_id__icontains=q)
    else:
        bookingdetailss=BookingDetails.objects.all()
    return render(request,'app/bookinghistory.html' , {'bookingdetailss':bookingdetailss})


@login_required
@manager_only
def aftercompleted(request):
    if 'q' in request.GET:
        q=request.GET['q']
        bookinghistorys=BookingHistory.objects.filter(trip_type__icontains=q)
    else:
        bookinghistorys=BookingHistory.objects.all()
    return render(request,'app/aftercompleted.html' , {'bookinghistorys':bookinghistorys})


@login_required
@manager_only
def bookingdetails(request):
    bookingdetailss=BookingDetails.objects.all()
    return render(request,'app/bookingdetails.html' , {'bookingdetailss':bookingdetailss})

@login_required
@manager_only
def customeruser(request):
    temp=CustomerUser.objects.all()
    form2= OrderFilter2(request.GET, queryset=temp)
    customerusers = form2.qs

    return render(request,'app/customeruser.html' , {'customerusers':customerusers,'form2':form2})



    

@login_required
@manager_only
def alluser(request):
    if 'q' in request.GET:
        q=request.GET['q']
        admin=Admin.objects.filter(name__icontains=q)
    else:
        admin = Admin.objects.all()
    return render(request,'app/alluser.html',{'admin':admin})


@login_required
@manager_only
def notification(request):
    noti=Notification.objects.all().order_by('-date')
    return render(request,'app/notification.html', {'noti':noti})


@login_required
@manager_only
def coupons(request):
    coup=Coupons.objects.all()
    return render(request,'app/coupons.html', {'coup':coup})

@login_required
@manager_only
def brand(request):
    bran=Brand.objects.all()
    return render(request,'app/brand.html', {'bran':bran})

@login_required
@manager_only
def brandmodel(request):
    branm=BrandModel.objects.all()
    return render(request,'app/brandmodel.html', {'branm':branm})

@login_required
@manager_only
def insurance(request):
    insu=Insurance.objects.all()
    return render(request,'app/insurance.html', {'insu':insu})

@login_required
@manager_only
def drivers_verify(request):
    if 'q' in request.GET:
        q=request.GET['q']
        drivers=Driver.objects.filter(driver_name__icontains=q)
        drivers=drivers.filter(status='UNDER VARIFICATION')
    else:
        drivers=Driver.objects.all().filter(status='UNDER VARIFICATION')
    return render(request, 'app/drivers_verify.html',{'drivers':drivers})


@login_required
@manager_only
def booking_request(request):
    bookingdetailss=BookingDetails.objects.all().filter(assign_driver=None).filter(reject=False)
    return render(request,'app/booking_request.html' , {'bookingdetailss':bookingdetailss})


def profile(request):
    return render(request, 'app/profile.html')


@login_required
@manager_only
def today(request):
    date=datetime.date.today()
    bookingdetailss=BookingDetails.objects.all().filter(drop_date=date)
    return render(request,'app/today.html' , {'bookingdetailss':bookingdetailss})

@login_required
@manager_only
def week(request):
    date=datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    bookingdetailss=BookingDetails.objects.all().filter(drop_date__range=[start_week, end_week])
    return render(request,'app/week.html' , {'bookingdetailss':bookingdetailss})

@login_required
@manager_only
def month(request):
    date=datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(30)
    bookingdetailss=BookingDetails.objects.all().filter(drop_date__range=[start_week, end_week])
    return render(request,'app/month.html' , {'bookingdetailss':bookingdetailss})


######EDIT#########


@login_required
@manager_only
def editdriver(request, pk):
    driver = Driver.objects.get(driver_id=pk)
    form = DriverEditFrom(instance=driver)
    if request.method == 'POST':
        form = DriverEditFrom(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('drivers_verify')
    return render(request,'app/editdriver.html', {'form':form})

@login_required
@manager_only
def edituser(request, pk):
    customeruser = CustomerUser.objects.get(id=pk)
    form = CustomerUserFrom(instance=customeruser)
    if request.method == 'POST':
        form = CustomerUserFrom(request.POST, instance=customeruser)
        if form.is_valid():
            form.save()
            return redirect('customeruser')
    return render(request,'app/edituser.html', {'form':form})


@login_required
@manager_only
def assigndriver(request, pk):
    booking = BookingDetails.objects.get(booking_id=pk)
    form = AssignDriverForm(instance=booking)
    temp=Driver.objects.all()
    form2= OrderFilter(request.GET, queryset=temp)
    drivers = form2.qs

    if request.method == 'POST':
        form = AssignDriverForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_request')
    return render(request,'app/assign_driver.html', {'form':form,'form2': form2,'drivers': drivers,'pk':pk})

def assigndriver2(request, pk, pk2):
    booking = BookingDetails.objects.get(booking_id=pk)
    driver= Driver.objects.get(driver_id=pk2)
    booking.assign_driver = driver
    booking.save()
    return redirect('booking_request')
  


@login_required
@manager_only
def rejectdriver(request, pk):
    booking = BookingDetails.objects.get(booking_id=pk)
    form = RejectDriverForm(instance=booking)
    if request.method == 'POST':
        form = RejectDriverForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_request')
    return render(request,'app/rejectdriver.html', {'form':form})
  



##########DELETE############


@login_required
@manager_only
def deletedriver(request, pk):
	driver = Driver.objects.get(driver_id=pk)
	if request.method == "GET":
		driver.delete()
		return redirect('driver')



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
    obj=get_object_or_404(CustomerUser,id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('customeruser')


@login_required
@manager_only
def deletenotification(request,pk):
    obj=get_object_or_404(Notification,id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('notification')


@login_required
@manager_only
def editcontact(request):
    temp = Contact.objects.get(id=1)
    form = ContactEditForm(instance=temp)
    if request.method == 'POST':
        form = ContactEditForm(request.POST, instance=temp)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'app/editcontact.html', {'form':form})



#######CREATE###########

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
def createcoupons(request):
    temp=CustomerUser.objects.all()
    form2= OrderFilter2(request.GET, queryset=temp)
    customerusers = form2.qs
    form = CouponsFrom()
    if request.method == 'POST':
        form = CouponsFrom(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('coupons')
    return render(request,'app/createcoupons.html', {'form':form,'form2':form2,'customerusers':customerusers})



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
def createbrand(request):
    form = BrandFrom()
    if request.method == 'POST':
        form = BrandFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand')
    return render(request,'app/createbrand.html', {'form':form})


@login_required
@manager_only
def createbrandmodel(request):
    form = BrandModelFrom()
    if request.method == 'POST':
        form = BrandModelFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brandmodel')
    return render(request,'app/createbrandmodel.html', {'form':form})

@login_required
@manager_only
def createinsurance(request):
    form = InsuranceFrom()
    if request.method == 'POST':
        form = InsuranceFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insurance')
    return render(request,'app/createinsurance.html', {'form':form})


@login_required
@manager_only
def createfrompoint(request):
    form = FrompointForm()
    form2=Frompoint.objects.all()
    if request.method == 'POST':
        form = FrompointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createfrompoint')
    return render(request,'app/createfrompoint.html', {'form':form,'form2':form2})


