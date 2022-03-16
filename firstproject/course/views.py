from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def index(request):
#     return HttpResponse('Home Page')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('Hello Python')

def learn_variable(request):
    var = '<h1>Hello Variable</h1>'
    return HttpResponse(var)

def learn_math(request):
    num = 7 + 7
    return HttpResponse(f'7 + 7 = {num}')