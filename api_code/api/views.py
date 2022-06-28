from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import ProductSerializers, CustomerSerializers, CustomerMultipleProductSerializers, CustomerMultiProductSerializer
from .models import Product, Customer, CustomerMultipleProduct
from rest_framework import status
from django.shortcuts import get_object_or_404
import json
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


class CustomerMultiProduct(APIView):
    
    def get(self, request, pk=None, *args, **kwargs):
        try:
            if pk is not None:
                customer_instance = get_object_or_404(CustomerMultipleProduct,pk=pk)
                print(customer_instance)
                serializer = CustomerMultiProductSerializer(customer_instance)
                content = {
                    "Status":status.HTTP_200_OK,
                    "Data":serializer.data
                }
                return Response(content,status=status.HTTP_200_OK)
            else:
                customer_instance = CustomerMultipleProduct.objects.all()
                print(customer_instance)
                serializer = CustomerMultiProductSerializer(customer_instance,many=True)
                content = {
                    "Status":status.HTTP_200_OK,
                    "Data":serializer.data
                }
                return Response(content,status=status.HTTP_200_OK)
        except Exception as exception:
            content = {
                "Status":status.HTTP_400_BAD_REQUEST,
                "Data":[]
            }
            return Response(content,status=status.HTTP_400_BAD_REQUEST)



