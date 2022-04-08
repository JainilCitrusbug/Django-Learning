from django.urls import path, include
from API import model_viewset_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', model_viewset_views.UserModelViewSetAPI, basename='user')
router.register('product', model_viewset_views.ProductModelViewSetAPI, basename='product')
router.register('category', model_viewset_views.CategoryModelViewSetAPI, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]