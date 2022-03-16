from pyexpat import model
from re import template
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import student, info
from .forms import StudentRegistrationForm
# Create your views here.

class StudentListView(ListView):
    model = student
    # ordering = ['name']
    template_name = 'application/student.html'
    context_object_name = 'students'    

    # def get_queryset(self):
    #     return student.objects.filter(course = 'python')

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['freshers'] = student.objects.all().order_by('name')
    #     return context


class StudentDetailsView(DetailView):
    model = student
    template_name = 'application/student2.html'
    context_object_name = 'student2'
    pk_url_kwarg = 'id'


# def showformdata(request):
#     fm = StudentRegistrationForm()
#     # fm = StudentRegistrationForm(auto_id=True, label_suffix=' :- ', initial={'name':'jainil', 'email':'jainil@gmail.com', 'number':'0123456789', 'course':'Django'})
#     # Manually assign order of field
#     fm.order_fields(field_order=['name', 'email', 'number', 'course'])
#     return render(request, 'application/data.html', {'form':fm})



# # Function Based
# def showformdata(request):
#     if request.method=='POST':
#         fm = StudentRegistrationForm(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             email = fm.cleaned_data['email']
#             number = fm.cleaned_data['number']
#             course = fm.cleaned_data['course']
#             reg = info(name=name, email=email, number=number, course=course)
#             reg.save()
#             return render(request, 'application/success.html', {'name': name, 'email':email, 'number':number, 'course':course})
#     else:
#         fm = StudentRegistrationForm()
#     return render(request, 'application/data.html', {'form':fm})



# Class based
class ShowFormData(View):
    def get(self, request):
        fm = StudentRegistrationForm()
        return render(request, 'application/data.html', {'form':fm})
    
    def post(self, request):
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            number = fm.cleaned_data['number']
            course = fm.cleaned_data['course']
            reg = info(name=name, email=email, number=number, course=course)
            reg.save()
            return render(request, 'application/success.html', {'name': name, 'email':email, 'number':number, 'course':course})
