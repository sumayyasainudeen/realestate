from tradersApp import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('admin_home_page',views.admin_home_page,name='admin_home_page'),
    path('add_property',views.add_property,name='add_property'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('property_profile/<int:id>',views.property_profile,name='property_profile'),
    path('property_profile_tenant/<int:id>',views.property_profile_tenant,name='property_profile_tenant'),
    path('Booking/<int:id>',views.Booking,name='Booking'),
    path('profile',views.profile,name='profile'),
    path('properties',views.properties,name='properties'),
    path('view_unit/<int:id>',views.view_unit,name='view_unit'),
    path('logout',views.logout,name='logout'),
]