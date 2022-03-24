from pyexpat import model
from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
# Create your views here.

class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            category_menu = Category.objects.all()
            product = Product.objects.all().order_by('id')
            paginator = Paginator(product, 5)
            page_number = request.GET.get('page')
            page_object = paginator.get_page(page_number)
            return render(request, 'index.html', {'page_object' : page_object,'category_menu':category_menu})
        else:
            return redirect('/login/')

class Details(DetailView):
    model = Product
    template_name = 'details.html'
    context_object_name = 'productview'
    pk_url_kwarg = 'id'


class LogIn(View):
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

class SignUp(View):
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

class UserProduct(View):
    def get(self,request):
        if request.user.is_authenticated:
            # product = Product.objects.all().order_by('id')
            category_menu = Category.objects.all()
            user = User.objects.get(username=request.user.username)
            return render(request, 'userproduct.html', {'user' : user,'category_menu':category_menu})
        else:
            return redirect('/login/')

class Profile(View):
    def get(self, request):
        category_menu = Category.objects.all()
        return render(request, 'profile.html', {'category_menu':category_menu})

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class AddProduct(View):
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
        image = request.FILES['photo']
        category = request.POST['category']
        category_object = Category.objects.get(category_name=category)
        users = User.objects.get(id=request.user.id)  
        pd = Product(product_name=title,product_description=description,product_price=price,product_image=image,product_category=category_object,user=users)
        pd.save()
        return redirect('/userproduct/')

class AddCategory(View):
    def get(self, request):
        category_menu = Category.objects.all()
        return render(request, 'addcategory.html',{'category_menu':category_menu})

    def post(self, request):
        category = request.POST['category']
        category_object = Category.objects.filter(category_name=category)

        if not category_object.exists():
            cd = Category(category_name=category)
            cd.save()
        
        return redirect('/addproduct/')

class EditProduct(UpdateView):
    model = Product
    fields = ['product_name','product_description','product_price','product_category','product_image']
    template_name = 'editproduct.html'
    pk_url_kwarg = 'id'
    success_url ="/userproduct/"

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'deleteproduct.html'
    pk_url_kwarg = 'id'
    success_url ="/userproduct/"

class SearchProduct(View):
    def get(self, request):
        category_menu = Category.objects.all()
        searched = request.GET.get('search')
        product_searched = Product.objects.filter(product_name__icontains=searched)
        return render(request, 'searchproduct.html', {'searched':searched,'product_searched':product_searched,'category_menu':category_menu})


class CategoryView(View):
    def get(self, request, categories):
        category_menu = Category.objects.all()
        product = Product.objects.filter(product_category__category_name=categories)
        return render(request, 'category.html',{'categories':categories,'product':product,'category_menu':category_menu})

