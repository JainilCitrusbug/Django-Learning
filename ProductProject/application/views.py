from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            products = Product.objects.filter(soft_delete = False).order_by('id')
            product = products.order_by('id')
            count_product = products.count()
            category_menu = Category.objects.all()
            paginator = Paginator(product, 5)
            page_number = request.GET.get('page')
            page_object = paginator.get_page(page_number)
            return render(request, 'index.html', {'page_object' : page_object,'category_menu':category_menu,'count_product':count_product})
        else:
            return redirect('/login/')

class DetailsView(DetailView):
    model = Product
    template_name = 'details.html'
    context_object_name = 'productview'
    pk_url_kwarg = 'id'


class LogInView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('/')

    def post(self, request):
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username = username, password = password1)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')

class SignUpView(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('/login/')

class UserProductView(View):
    def get(self,request):
        if request.user.is_authenticated:
            count_product = Product.objects.filter(user=request.user.id, soft_delete = False).count()
            category_menu = Category.objects.all()
            user = User.objects.get(username=request.user)
            return render(request, 'userproduct.html', {'user' : user,'category_menu':category_menu,'count_product':count_product})
        else:
            return redirect('/login/')

class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            category_menu = Category.objects.all()
            return render(request, 'profile.html', {'category_menu':category_menu})
        else:
            return redirect('/login/')

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class AddProductView(View):
    def get(self, request):
        category_menu = Category.objects.all()
        if request.user.is_authenticated:
            return render(request, 'addProduct.html',{'category_menu':category_menu})
        else:
            return redirect('/login/')

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES.get('photo')
        category = request.POST['category']
        category_object = Category.objects.get(category_name=category)
        users = User.objects.get(id=request.user.id)  
        pd = Product(product_name=title,product_description=description,product_price=price,product_image=image,product_category=category_object,user=users)
        pd.save()
        return redirect('/userproduct/')

class AddCategoryView(View):
    def get(self, request):
        category_menu = Category.objects.all()
        if request.user.is_authenticated:
            return render(request, 'addcategory.html',{'category_menu':category_menu})
        else:
            return redirect('/login/')

    def post(self, request):
        category = request.POST['category']
        category_object = Category.objects.filter(category_name=category)

        if not category_object.exists():
            cd = Category(category_name=category)
            cd.save()
        
        return redirect('/addproduct/')

class EditProductView(UpdateView):
    model = Product
    fields = ['product_name','product_description','product_price','product_category','product_image']
    template_name = 'editproduct.html'
    pk_url_kwarg = 'id'
    success_url ="/userproduct/"

# class DeleteProductView(DeleteView):
#     model = Product
#     template_name = 'deleteproduct.html'
#     pk_url_kwarg = 'id'
#     success_url ="/userproduct/"

class DeleteProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.soft_delete = True
        product.save()
        return redirect('/userproduct/')
        

class SearchProductView(View):
    def get(self, request):
        category_menu = Category.objects.all()
        searched = request.GET.get('search')
        product_searched = Product.objects.filter(Q(product_name__icontains=searched) | Q(product_description__icontains=searched) | Q(product_price__icontains=searched), soft_delete = False)
        product_searched_json = serializers.serialize('json', product_searched)
        count_product = product_searched.count()
        # data = {
        #     # 'searched':searched,
        #     'product_searched':product_searched_json,
        #     # 'category_menu':category_menu,
        #     # 'count_product':count_product
        #     }
        print(product_searched_json)
        # return render(request, 'searchproduct.html', data)
        return JsonResponse(product_searched_json, safe=False)


class CategoryView(View):
    def get(self, request, categories):
        category_menu = Category.objects.all()
        product = Product.objects.filter(product_category__category_name=categories, soft_delete = False)
        count_product = product.count()
        return render(request, 'category.html',{'categories':categories,'product':product,'category_menu':category_menu,'count_product':count_product})

