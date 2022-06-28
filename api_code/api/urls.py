from django.urls import path 
from .views import api_home, api_m2m, CustomerMultiProduct

urlpatterns = [

    path("",api_home),
    path("m2m",api_m2m),
    path('customer/',CustomerMultiProduct.as_view()),
    path('customer/<int:pk>/',CustomerMultiProduct.as_view()),
    
]