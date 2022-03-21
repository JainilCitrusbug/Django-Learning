from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Index(View):
    def get(self,request):
        return render(request, 'index.html')

class LogIn(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return HttpResponseRedirect('/profile/')

    def post(self, request):
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username = username, password = password1)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/profile/')
        else:
            return HttpResponseRedirect('/login/')

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
        return HttpResponseRedirect('/login/')

class Profile(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'profile.html')
        else:
            return HttpResponseRedirect('/login/')

class LogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class AddProduct(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'addProduct.html')
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        return HttpResponseRedirect('/profile/')