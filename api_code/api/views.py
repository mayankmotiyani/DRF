from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import ProductSerializers, CustomerSerializers, CustomerMultipleProductSerializers
from .models import Product, Customer, CustomerMultipleProduct
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def api_home(request):
    if request.method == 'GET':
        instance = Customer.objects.all()
        serializer = CustomerSerializers(instance,many=True)
        # here you will get orderedDict that returns returnList object
        """ you can use orderedDict to iterate over it """
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid(): # you can pass raise_exception = True or False
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


api_view(['GET','POST'])
def api_m2m(request):
    if request.method == 'GET':
        instance = CustomerMultipleProduct.objects.all()
        print(instance)
        serializer = CustomerMultipleProductSerializers(instance,many=True)
        # here you will get orderedDict that returns returnList object
        """ you can use orderedDict to iterate over it """
        return JsonResponse({"Data":serializer.data})
    elif request.method == 'POST':
        serializer = CustomerMultipleProductSerializers(data=request.data)
        if serializer.is_valid(): # you can pass raise_exception = True or False
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


