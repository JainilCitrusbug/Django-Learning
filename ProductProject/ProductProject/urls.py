"""ProductProject URL Configuration

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
from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('addproduct/', views.AddProduct.as_view(), name='addproduct'),
    path('addcategory/', views.AddCategory.as_view(), name='addcategory'),
    path('details/<int:id>/',views.Details.as_view(), name = 'details'),
    path('edit/<int:id>/', views.EditProduct.as_view(), name='edit')
]
