from django.shortcuts import render
from django.http import HttpResponse
from application.models import student
from django.core.paginator import Paginator
# Create your views here.


def home(request):
    std = student.objects.all().order_by('id')
    paginator = Paginator(std, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_object' : page_object})