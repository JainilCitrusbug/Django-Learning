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
from .pagination import ProductPagination

# Create your views here.

#-----------------------------------------------------------------------------------------------------------
#User API
#-----------------------------------------------------------------------------------------------------------

class UserAPI(APIView):
    def get(self, request, id=None):
        search = request.GET.get('search')
        users = User.objects
        try:
            if id is not None:
                user = users.get(id=id)
                serializer = UserSerializers(user)
            elif search:
                user = users.filter(username__icontains = search)
                serializer = UserSerializers(user,many=True)
            else:
                user = users.all()
                serializer = UserSerializers(user,many=True)
        except:
            return JsonResponse('Data does not exist......', safe=False)
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

#-----------------------------------------------------------------------------------------------------------
#Product API
#-----------------------------------------------------------------------------------------------------------

class ProductAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = ProductPagination
    

    def get(self, request, id=None):
        search = request.GET.get('search')
        filter = request.GET.get('filter')
        page = request.GET.get('page') 
        products = Product.objects
        try:
            if id is not None:
                product = products.get(id=id)
                serializer = ProductSerializers(product)
            elif search:
                product = products.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search) | Q(product_category__category_name__icontains=search) | Q(product_price__icontains=search))
                serializer = ProductSerializers(product,many=True)
            elif filter:
                product = products.filter(product_category__category_name = filter)
                serializer = ProductSerializers(product,many=True)
            elif page:
                product = products.all()
                paginator = Paginator(product, 2)
                page_object = paginator.get_page(page)
                serializer = ProductSerializers(page_object,many=True)
            else:
                product = products.all()
                serializer = ProductSerializers(product,many=True)
        except:
            return JsonResponse('Data does not exist......', safe=False)
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
        categories = Category.objects
        try:
            if id is not None:
                category = categories.get(id=id)
                serializer = CategorySerializers(category)
            elif search:
                category = categories.filter(category_name__icontains = search)
                serializer = CategorySerializers(category,many=True)
            else:
                category = categories.all()
                serializer = CategorySerializers(category,many=True)
        except:
            return JsonResponse('Data does not exist......', safe=False)
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

