from unicodedata import name
from django.urls import path
from . import views


app_name = 'login'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('confirm/', views.user_confirm, name='user_confirm')
]
