from django.urls import path 
from .views import api_home, api_m2m

urlpatterns = [

    path("",api_home),
    path("m2m",api_m2m)
    
]