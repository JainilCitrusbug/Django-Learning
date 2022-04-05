from django.urls import path
from API.views import *

urlpatterns = [
    path('product/', ProductAPI.as_view(), name='product'),
    path('product/<int:id>', ProductAPI.as_view(), name='product'),
]