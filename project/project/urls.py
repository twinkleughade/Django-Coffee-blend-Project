"""
URL configuration for project project.

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('home1/<int:pk>',views.home1,name='home1'),
    path('about/',views.about,name='about'),
    path('menu/',views.menu,name='menu'),
    path('service/',views.service,name='service'),
    path('register/',views.register,name='register'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('order_online/',views.order_online,name='order_online'),
    path('logindata/',views.logindata,name='logindata'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('first/',views.first,name='first'),
    path('asc/',views.asc,name='asc'),
    path('last_5/',views.last_5,name='last_5'),
    path('desc/',views.desc,name='desc'),
    path('all/',views.all,name='all')

    
]
