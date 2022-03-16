from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learnV/', views.learn_variable),
    path('learnM/', views.learn_math),
]