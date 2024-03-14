from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.http import Http404
from django.db.models import Sum

# Create your views here.

#user registration
class RegisterAPIView(APIView):
    def get(self, request):
        registers = register.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#user login  
class usersigninview(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get('username')
            password=serializer.validated_data.get('password')

            b=register.objects.all()
            for i in b:
                if username==i.username and password==i.password:
                    return Response({'msg':'logged in successfully'})
            else:
                return Response({'msg':'login failed'})
            
#product creation
class ProductAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#product update,retrive,delete
class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#order
class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#view for listing highest ordered product
class ProductOrderListView(APIView):
    def get(self, request, *args, **kwargs):
        
        product_quantity = Order.objects.values('product').annotate(total_quantity=Sum('quantity'))
        sorted_products = sorted(product_quantity, key=lambda x: x['total_quantity'], reverse=True)
        product_list = []
        for item in sorted_products:
            product = Product.objects.get(id=item['product'])
            product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'size': product.size,
                'color': product.color,
                'total_quantity': item['total_quantity']
            }
            product_list.append(product_data)

        return Response(product_list)
        