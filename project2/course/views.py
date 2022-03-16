from django.shortcuts import render

# Create your views here.

def learn_django(request):
    details = {
        'firstname' : 'Jainil',
        'lastname' : 'Prajapati',
    }
    return render(request, 'course.html', details)

def learn_python(request):
    return render(request, 'course2.html')