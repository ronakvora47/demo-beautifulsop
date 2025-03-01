"""
URL configuration for WebScrapping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('scrape-titles/', views.scrape_titles, name='scrape_titles'),
    path('hello/', views.hello, name='hello'),
    path('fun/', views.fun, name='fun'),
    path('main/', views.main, name='main'),
    path('ronak/', views.ronak, name='ronak'),
    
]
