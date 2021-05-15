from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import generics ,  permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from app.models import *
from .Serializers import *
from django.http import HttpResponse

def home(request):
    return JsonResponse({'Driver':'/api/driver','Customer':'/api/customeruser','vehicle':'/api/vehicle','bookingdetails':'/api/bookingdetails','bookinghistory':'/api/bookinghistory','notification':'/api/notification','coupons':'/api/coupons',})



class DriverList(generics.ListCreateAPIView):
    queryset=Driver.objects.all()
    serializer_class=DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save()


class CustomerUserList(generics.ListCreateAPIView):
    queryset=CustomerUser.objects.all()
    serializer_class=CustomerUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()

class VehicleList(generics.ListCreateAPIView):
    queryset=Vehicle.objects.all()
    serializer_class=VehicleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()

class BookingDetailsList(generics.ListCreateAPIView):
    queryset=BookingDetails.objects.all()
    serializer_class=BookingDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()


class BookingHistoryList(generics.ListCreateAPIView):
    queryset=BookingHistory.objects.all()
    serializer_class=BookingHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()


class notificationList(generics.ListCreateAPIView):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()


class CouponsList(generics.ListCreateAPIView):
    queryset=Coupons.objects.all()
    serializer_class=CouponsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()