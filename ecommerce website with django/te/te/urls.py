"""
URL configuration for tes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
from django.contrib import admin
from django.urls import path
from ao import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),  # default login

    # Auth
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    # User Side
    path('home/', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/<int:product_id>/', views.order, name='order'),
    path('orders/', views.orders, name='orders'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    # Admin Side
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-product/', views.add_product, name='add_product'),
    path('all-orders/', views.all_orders, name='all_orders'),
    path('all-users/', views.all_users, name='all_users'),
]




