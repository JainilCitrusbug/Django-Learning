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
from django.urls import path, include
from application import views
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='CRUD API',
        default_version="v1",
        description='Test 1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('userproduct/', views.UserProductView.as_view(), name='userproduct'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('addproduct/', views.AddProductView.as_view(), name='addproduct'),
    path('addcategory/', views.AddCategoryView.as_view(), name='addcategory'),
    path('details/<int:id>/',views.DetailsView.as_view(), name = 'details'),
    path('edit/<int:id>/', views.EditProductView.as_view(), name='edit'),
    path('delete/<int:id>/', views.DeleteProductView.as_view(), name='delete'),
    path('search/', views.SearchProductView.as_view(), name='search'),
    path('category/<str:categories>/', views.CategoryView.as_view(), name='category'),

    
    path('api/', include('API.urls')),
    path('modelapi/', include('API.model_viewset_urls')),

    
    path('swagger-ui/', schema_view.with_ui('swagger', cache_timeout=0), name='openapi-schema'),


    path('customadmin/', include('customadmin.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
