from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError

# Create your models here.
class Tenants(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,default='',null=True,blank=True)
    phone=models.IntegerField(default=0)
    document= models.ImageField(upload_to="image/", null=True)
    image= models.ImageField(upload_to="image/", null=True)


class Properties(models.Model):
    
    name=models.CharField(max_length=255,default='',null=True,blank=True)
    address=models.CharField(max_length=255,default='',null=True,blank=True)
    location=models.CharField(max_length=255,default='',null=True,blank=True)
    phone=models.CharField(max_length=255,default='',null=True,blank=True)
    Features=models.CharField(max_length=255,default='',null=True,blank=True)
    property_image= models.ImageField(upload_to="image/", null=True)

class Units(models.Model):
    assigned_tenant=models.ForeignKey(Tenants,on_delete=models.CASCADE,default='',null=True)
    property=models.ForeignKey(Properties,on_delete=models.CASCADE,null=True)
    rent=models.IntegerField(default=0)
    type=models.CharField(max_length=255,default='',null=True,blank=True)
    image= models.ImageField(upload_to="image/", null=True)
    Features=models.CharField(max_length=220)

class Rental_information(models.Model):
    unit=models.ForeignKey(Units,on_delete=models.CASCADE,null=True)
    tenant=models.ForeignKey(Tenants,on_delete=models.CASCADE,null=True)
    agreemented_date=models.DateField(auto_now=True,null=True)
    start_date=models.DateField(auto_now=False,null=True)
    end_date=models.DateField(auto_now=False,null=True)
    rent_date=models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    


