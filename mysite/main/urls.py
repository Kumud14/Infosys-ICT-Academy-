from django.urls import path
from . import views 
from main.views import home,edit,delete

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
]
