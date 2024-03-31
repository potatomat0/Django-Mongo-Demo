from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from products.models import product
from products.serializers import productSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    if request.method == 'GET':
        products = product.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            products = products.filter(title__icontains=title)
        
        products_serializer = productSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
 
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = productSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = product.objects.all().delete()
        return JsonResponse({'message': '{} products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try: 
        product = product.objects.get(pk=pk) 
    except product.DoesNotExist: 
        return JsonResponse({'message': 'Sản phẩm không tồn tại'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        product_serializer = productSerializer(product) 
        return JsonResponse(product_serializer.data) 
 
    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        product_serializer = productSerializer(product, data=product_data) 
        if product_serializer.is_valid(): 
            product_serializer.save() 
            return JsonResponse(product_serializer.data) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        product.delete() 
        return JsonResponse({'message': 'sản phẩm bị xóa thành công!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def product_list_by_category(request, category):
    """
    Lấy danh sách sản phẩm theo danh mục.
    """
    products = product.objects.filter(category=category)  
        
    if request.method == 'GET': 
        products_serializer = productSerializer(products, many=True)  
        return JsonResponse(products_serializer.data, safe=False)
    
