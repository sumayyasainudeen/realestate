from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from datetime import timedelta, date

from tradersApp.models import *


# Create your views here.
def index(request):
     all_properties = Properties.objects.all()
     context = {
         'all_properties':all_properties,
     }
     return render(request,'index.html',context)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home_page')
            else:
                login(request, user)
                auth.login(request, user)
                # messages.success(request,' Welcome...'+ user.first_name)
                return redirect('index')
        else:
            messages.info(request,'Please Register First!')
    return redirect('index')

def admin_home_page(request):
     all_properties = Properties.objects.all()
     context = {
         'all_properties':all_properties,
     }
     return render(request,'admin_home_page.html',context)

def add_property(request):
    if request.method == 'POST':
        name = request.POST['property_name']
        address = request.POST['address']
        location = request.POST['location']
        number = request.POST['number']
        features = request.POST['featurs']
        image = request.FILES['image'] if 'image' in request.FILES else None

        property_instance = Properties(name=name,address=address,location=location,phone=number,Features=features, property_image=image)
        property_instance.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_unit(request):
    if request.method == 'POST':
        propertyId = request.POST['property']
        type = request.POST['type']
        rent = request.POST['rent']
        features = request.POST['featurs']
        image = request.FILES['image'] if 'image' in request.FILES else None

        unit_instance = Units(property_id=propertyId,rent=rent,type=type,Features=features, image=image)
        unit_instance.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def property_profile(request,id):
     property = Properties.objects.get(id=id)
     all_units = Units.objects.filter(property=property)
     unit_count = Units.objects.filter(property=property).count()
     context = {
         'property':property,
         'all_units':all_units,
         'unit_count':unit_count,
     }
     return render(request,'property_profile.html',context)

def property_profile_tenant(request,id):
     property = Properties.objects.get(id=id)
     all_units = Units.objects.filter(property=property)
     unit_count = Units.objects.filter(property=property).count()
     context = {
         'property':property,
         'all_units':all_units,
         'unit_count':unit_count,
     }
     return render(request,'property_profile_tenant.html',context)

def sign_up(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        add = request.POST['address']
        email = request.POST['email']
        ph = request.POST['phonenumber']
        password = request.POST['password']
        profile = request.FILES['file1'] if 'file1' in request.FILES else None
        document = request.FILES['file2'] if 'file2' in request.FILES else None
      

            
        if User.objects.filter(email=email).exists():
          messages.warning(request,'This Email Already Exists!')
          return redirect('index')
        else:
          user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=email,password=password)
          user.save()

          data = User.objects.get(id=user.id)
          tenant = Tenants(address=add,phone=ph,document=document,image=profile,user=data)
          tenant.save()
          messages.success(request,'Registered Successfully!')
          return redirect('index')


   
    else:
        return redirect('index')

def Booking(request,id):
    current_user = request.user
    current_id = current_user.id
    unit = Units.objects.get(id=id)
    if request.method == 'POST':
        Start_date = request.POST['start']
        end_date = request.POST['end']
        rent_date = request.POST['rent_date']
        
        tenant = Tenants.objects.get(user_id=current_id)
        booking = Rental_information(unit=unit,tenant=tenant,start_date=Start_date,end_date=end_date,rent_date=rent_date)
        booking.save()
    unit.assigned_tenant=tenant
    unit.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def profile(request):
     current_user = request.user
     current_id = current_user.id
     tenant = Tenants.objects.get(user_id=current_id)
     Rental_info = Rental_information.objects.filter(tenant=tenant)
     
     context = {
         'tenant':tenant,
         'Rental_info':Rental_info,
     }
     return render(request,'profile.html',context)

def properties(request):
     current_user = request.user
     current_id = current_user.id
     all_property = Properties.objects.all()
     all_units = Units.objects.all()
     context = {
         'all_property':all_property,
         'all_units':all_units
     }
     return render(request,'properties.html',context)

def view_unit(request,id):
     unit = Units.objects.get(id=id)
     context = {
         'unit':unit,
        
     }
     return render(request,'view_unit.html',context)
    

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')
