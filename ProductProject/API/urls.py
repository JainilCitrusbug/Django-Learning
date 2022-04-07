from django.urls import path
from API.views import *

urlpatterns = [
    #-----------------------------------------------------------------------------------------------------------
    #User URL
    #-----------------------------------------------------------------------------------------------------------

    path('user/', UserAPI.as_view(), name='user'),
    path('user/<int:id>', UserAPI.as_view(), name='user'),

    #-----------------------------------------------------------------------------------------------------------
    #Product URL
    #-----------------------------------------------------------------------------------------------------------

    path('product/', ProductAPI.as_view(), name='product'),
    path('product/<int:id>', ProductAPI.as_view(), name='product'),

    #-----------------------------------------------------------------------------------------------------------
    #Product URL
    #-----------------------------------------------------------------------------------------------------------

    path('category/', CategoryAPI.as_view(), name='category'),
    path('category/<int:id>', CategoryAPI.as_view(), name='category'),
]