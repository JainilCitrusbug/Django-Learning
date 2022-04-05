from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from application.models import *
from API.serializers import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ProductAPI(APIView):
    def get(self, request, id=None):
        if id is not None:
            product = Product.objects.get(id=id)
            serializer = ProductSerializers(product)
        else:
            product = Product.objects.all()
            serializer = ProductSerializers(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    def patch(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializers(product, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.soft_delete = True
        product.save()
        return JsonResponse('Deleted.......', safe=False)