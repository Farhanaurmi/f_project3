from django.db import models

class Driver(models.Model):
    driver_name=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=20, null=True)
    pin_code=models.CharField(max_length=10, null=True)
    mohalla_or_village=models.CharField(max_length=200, null=True)
    district=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)
    vehicle_registration_no=models.CharField(max_length=100, null=True)
    vehicle_brand=models.CharField(max_length=100, null=True)
    vehicle_model=models.CharField(max_length=100, null=True)
    insurance_validity=models.CharField(max_length=100, null=True)
    insurance_type=models.CharField(max_length=100, null=True)
    registration_year=models.CharField(max_length=10, null=True)
    km_driven=models.CharField(max_length=50, null=True)
    choice=(('UNDER VARIFICATION','UNDER VARIFICATION'),('ACTIVE','ACTIVE'),('OFFLINE','OFFLINE'),('ON A RIDE','ON A RIDE'))
    status=models.CharField(max_length=50, choices=choice, default='pending', null=True) 


    def __str__(self):
        return self.driver_name

class CustomerUser(models.Model):
    user_name=models.CharField(max_length=150, null=True)
    mobile_no=models.CharField(max_length=25, null=True)
    wallet_amount=models.CharField(max_length=10, null=True)
    email_id=models.EmailField(max_length=60, null=True, blank=True)
    User_Id=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user_name




