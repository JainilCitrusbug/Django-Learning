from unicodedata import category
from application.models import *
from API.serializers import *
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response


#-----------------------------------------------------------------------------------------------------------
#User API
#-----------------------------------------------------------------------------------------------------------

class UserModelViewSetAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request, *args, **kwargs):
        search = request.GET.get('search')
        user = User.objects.all()

        if search:
            user = user.filter(username__icontains = search)               
                               
        serializer = UserSerializers(user,many=True)
        return Response(serializer.data)


#-----------------------------------------------------------------------------------------------------------
#Product API
#-----------------------------------------------------------------------------------------------------------

class ProductModelViewSetAPI(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def list(self, request, *args, **kwargs):
        search = request.GET.get('search')
        filter = request.GET.get('filter')
        page = request.GET.get('page')
        product = Product.objects.filter(soft_delete=False)

        if search:
            product = product.filter(Q(product_name__icontains=search) | Q(product_description__icontains=search) | Q(product_category__category_name__icontains=search) | Q(product_price__icontains=search))
                
        if filter:
            product = product.filter(product_category__category_name = filter)                
                
        paginator = Paginator(product, 2)
        product = paginator.get_page(page)                   
        serializer = ProductSerializers(product,many=True)
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        product.soft_delete = True
        product.save()
        return Response('Deleted.......')

#-----------------------------------------------------------------------------------------------------------
#Category API
#-----------------------------------------------------------------------------------------------------------

class CategoryModelViewSetAPI(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def list(self, request, *args, **kwargs):
        search = request.GET.get('search')
        category = Category.objects.all()

        if search:
            category = category.filter(category_name__icontains = search)               
                               
        serializer = CategorySerializers(category,many=True)
        return Response(serializer.data)