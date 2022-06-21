from .models import Product, Customer, CustomerMultipleProduct
from rest_framework import serializers
from datetime import datetime



class ProductSerializers(serializers.ModelSerializer):
    created_time = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = "__all__"

    def get_created_time(self,obj): 
        return obj.get_time()

    """ Here you can use hasattr(obj,"id") and isinstance(obj,Product) """

class CustomerSerializers(serializers.ModelSerializer):
    """ Specific fields you can access or related with pk """
    product_name = serializers.ReadOnlyField(source='product.name')
    # product = ProductSerializers(read_only=True)
    # We can HyperlinkedRelatedField for represent the specific url that are callable
    class Meta:
        model = Customer
        fields = ["product","id","customer","delivered","created","updated","product_name"]
        # depth = 1


class CustomerMultipleProductSerializers(serializers.ModelSerializer):
    # product_m2m = serializers.SerializerMethodField()
    class Meta:
        model = CustomerMultipleProduct
        fields = ['id','customer','product']

    """ product_m2m use method to play with many to many fields """
    # def get_product_m2m(self,obj):
    #     productM2M = []
    #     get_qs = obj.product.get_queryset()
    #     for i in get_qs:
    #         productM2M.append(i.name)
    #     return productM2M
    
    """ Ways to handle m2m with detail """
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["product_m2m"] = ProductSerializers(instance.product.all(), many=True).data
        return data

    


        