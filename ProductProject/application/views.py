from pyexpat import model
from django.shortcuts import redirect, render
from django.http import Http404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class Index(ListView):
    model = Product
    template_name = 'index.html'
    ordering = ['id']
    paginate_by = 5

    def get_context_data(self, *args,**kwargs):
        try:
            return super(Index, self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(Index, self).get_context_data(*args,**kwargs)

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
            return redirect('/profile/')

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

class Profile(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'profile.html')
        else:
            return redirect('/login/')

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class AddProduct(View):
    def get(self, request):
        category_menu = Category.objects.all()

        if request.user.is_authenticated:
            return render(request, 'addProduct.html',{'menu':category_menu})
        else:
            return redirect('/login/')

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        category = request.POST['category']
        category_object = Category.objects.get(category_name=category)

        # if not category_object.exists():
        #     category_object= Category.objects.create(category_name=category)
        # else:
        #     category_object = Category.objects.get(category_name=category)
            
        pd = Product(product_name=title,product_description=description,product_price=price,product_category=category_object)
        pd.save()
        return redirect('/profile/')

class AddCategory(View):
    def get(self, request):
        return render(request, 'addcategory.html')

    def post(self, request):
        category = request.POST['category']
        category_object = Category.objects.filter(category_name=category)

        if not category_object.exists():
            cd = Category(category_name=category)
            cd.save()
        
        return redirect('/addproduct/')

class EditProduct(UpdateView):
    model = Product
    fields = ['product_name','product_description','product_price','product_category']
    template_name = 'editproduct.html'
    pk_url_kwarg = 'id'
    success_url ="/"

