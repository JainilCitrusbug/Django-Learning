from django.urls import path
from .. import views

app_name='customadmin'

urlpatterns = [
    # path('', views.CustomAdminLogInView.as_view(), name='customadminlogin'),
    # path('customadminlogout/', views.CustomAdminLogOutView.as_view(), name='customadminlogout'),
    # path('home/', CustomAdminHomePageView.as_view(), name='home'),

    # #-----------------------------------------------------------------------------------------------------------
    # #User URL
    # #-----------------------------------------------------------------------------------------------------------

    # path('userlist/', UserListView.as_view(), name='userlist'),
    # path('userlist/<int:id>/', UserDetailsView.as_view(), name='userlist'),

    # path('useredit/<int:id>/', UserUpdateView.as_view(), name='useredit'),

    # path('userdelete/<int:id>/', UserDeleteView.as_view(), name='userdelete'),

    # path('useradd/', UserCreationView.as_view(), name='useradd'),


    path("", views.IndexView.as_view(), name="dashboard"),
        # User
    # path("users/", views.UserListView.as_view(), name="user-detail"),

    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="user-detailview"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path("users/<int:pk>/password/", views.UserPasswordView.as_view(), name="user-password"),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),

    path("export_user_csv", views.export_user_csv, name="export_user_csv"),
    


    path("category/", views.CategoryListView.as_view(), name="category-list"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/detail/", views.CategoryDetailView.as_view(), name="category-detailview"),
    path("category/<int:pk>/update/", views.CategoryUpdateView.as_view(), name="category-update"),
    path("category/<int:pk>/delete/", views.CategoryDeleteView.as_view(), name="category-delete"),

    path("export_category_csv", views.export_category_csv, name="export_category_csv"),



    path("product/", views.ProductListView.as_view(), name="product-list"),
    path("product/create/", views.ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/detail/", views.ProductDetailView.as_view(), name="product-detailview"),
    path("product/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product-delete"),

    path("export_product_csv", views.export_product_csv, name="export_product_csv"),
]