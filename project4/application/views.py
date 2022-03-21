from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import student, info, Category, Product
from .forms import StudentRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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

# def signupform(request):
#     if request.method == 'POST':
#         fm = SignUp(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = SignUp()
#     return render(request, 'application/signup.html', {'form':fm})

class SignUpForm(View):
    def get(self, request):
        return render(request, 'application/signup.html')

    def post(self, request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return HttpResponseRedirect('/login/')


class LogInForm(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render (request, 'application/login.html')
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

class ProfilePage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'application/profile.html')
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        category = request.POST['category']
        category_object = Category.objects.filter(category_name=category).exists()
        
        if not category_object:
            category_object= Category.objects.create(category_name=category)
        pd = Product(product_name=title,product_description=description,product_price=price,product_category=category_object)
        pd.save()
        return HttpResponseRedirect('/profile/')

class UserLogOut(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')