"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django import views
from django.contrib import admin
from django.urls import path, include

"""
# Assign aliases to modules
from course import views as cv
from fees import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv.index),
    path('learndj/', cv.learn_django),
    path('learnpy/', cv.learn_python),
    path('learnV/', cv.learn_variable),
    path('learnM/', cv.learn_math),
    path('feesdj/', fv.fees_django),
    path('feespy/', fv.fees_python),

]
"""

"""
# Directly import functions
from course.views import index, learn_django, learn_python, learn_math, learn_variable
from fees.views import fees_django, fees_python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('learndj/', learn_django),
    path('learnpy/', learn_python),
    path('learnV/', learn_variable),
    path('learnM/', learn_math),
    path('feesdj/', fees_django),
    path('feespy/', fees_python),

]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
    path('fees/', include('fees.urls')),
]