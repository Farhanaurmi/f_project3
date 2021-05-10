from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
	name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	contact_no = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ['name', 'username','contact_no' , 'email', 'password1', 'password2']

class AdminForm(ModelForm):
	class Meta:
		model = Admin
		fields = '__all__'
		exclude = ['admin']

class DriverFrom(ModelForm):
	class Meta:
		model = Driver
		fields = '__all__'
		exclude = ['driver_id']

class CustomerUserFrom(ModelForm):
	class Meta:
		model = CustomerUser
		fields = '__all__'
		exclude = ['User_Id']


class VehicleFrom(ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'
		exclude = ['vehicle_id']

class NotificationFrom(ModelForm):
	class Meta:
		model = Notification
		fields = '__all__'


class CouponsFrom(ModelForm):
	class Meta:
		model = Coupons
		fields = '__all__'
