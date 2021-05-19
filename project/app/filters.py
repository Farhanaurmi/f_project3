import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Driver
		fields = ['driver_id','driver_name','mobile_no','mohalla_or_village','pin_code','status','district','state','vehicle_registration_no','vehicle_brand','vehicle_model','insurance_validity','insurance_type','registration_year','km_driven']
    


class OrderFilter2(django_filters.FilterSet):
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = CustomerUser
		fields = ['id','user_name','mobile_no','wallet_amount','email_id']