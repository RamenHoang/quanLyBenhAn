from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.do_login, name='login'),
    path('logout', views.do_logout, name='logout'),
]
