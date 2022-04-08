from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.core.paginator import Paginator
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from application.models import *
from API.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

#-----------------------------------------------------------------------------------------------------------
#User API
#-----------------------------------------------------------------------------------------------------------

class UserAPI(APIView):
    def get(self, request, id=None):
        search = request.GET.get('search')
        user = User.objects
        
        if id is not None:
            try:
                user = user.get(id=id)
                serializer = UserSerializers(user)
            except:
                return JsonResponse('Data does not exist......', safe=False)
        else:
            if search:
                user = user.filter(username__icontains = search)
                
            serializer = UserSerializers(user,many=True)
        return JsonResponse(serializer.data, safe=False)   

    @csrf_exempt
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors) 

    def patch(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializers(user, data = request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors)
        except:
            return JsonResponse('Data does not exist......', safe=False)

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse('User Deleted.........', safe=False)
        except:
            return JsonResponse('User does not exist......', safe=False)

#-----------------------------------------------------------------------------------------------------------
#Product API
#-----------------------------------------------------------------------------------------------------------

class ProductAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get(self, request, id=None):
        search = request.GET.get('search')
        filter = request.GET.get('filter')
        page = request.GET.get('page')
        
        if id is not None:
            try:
                product = Product.objects.get(id=id)
                serializer = ProductSerializers(product)
            except:
                return JsonResponse('Data does not exist......', safe=False)
        else:
            product = Product.objects.filter(soft_delete=False)

            if search:
                product = product.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search) | Q(product_category__category_name__icontains=search) | Q(product_price__icontains=search))
                
            if filter:
                product = product.filter(product_category__category_name = filter)                
                
            paginator = Paginator(product, 2)
            product = paginator.get_page(page)                   
            serializer = ProductSerializers(product,many=True)
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
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializers(product, data = request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors)
        except:
            return JsonResponse('Data does not exist......', safe=False)

    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product.soft_delete = True
            product.save()
            return JsonResponse('Deleted.......', safe=False)
        except:
            return JsonResponse('Data does not exist......', safe=False)

#-----------------------------------------------------------------------------------------------------------
#Category API
#-----------------------------------------------------------------------------------------------------------

class CategoryAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        search = request.GET.get('search')
        
        if id is not None:
            try:
                category = Category.objects.get(id=id)
                serializer = CategorySerializers(category)
            except:
                return JsonResponse('Data does not exist......', safe=False)
        else:
            category = Category.objects.all()
            if search:
                category = category.filter(category_name__icontains = search)
            
            serializer = CategorySerializers(category,many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        serializer = CategorySerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    def patch(self, request, id):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializers(category, data = request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors)
        except:
            return JsonResponse('Data does not exist......', safe=False)

    def delete(self, request, id):
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return JsonResponse('Category Deleted.........', safe=False)
        except:
            return JsonResponse('Data does not exist......', safe=False)