from django.shortcuts import render
from django.views import View
# Create your views here.

class index(View):
    def get(self,request):
        return render(request, 'index.html')

class login(View):
    def get(self,request):
        return render(request, 'login.html')

class signup(View):
    def get(self,request):
        return render(request, 'signup.html')

class profile(View):
    def get(self,request):
        return render(request, 'profile.html')