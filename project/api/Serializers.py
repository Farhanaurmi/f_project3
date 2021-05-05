from rest_framework import serializers
from app.models import *

class DriverSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Driver
        fields=['id','driver_name','mobile_no','pin_code','mohalla_or_village','district','state','vehicle_registration_no','vehicle_brand','vehicle_model','insurance_validity','insurance_type','registration_year','km_driven','status']

class CustomerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=CustomerUser
        fields=['id','user_name','mobile_no','wallet_amount','email_id','User_Id']


