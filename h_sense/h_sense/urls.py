"""
URL configuration for h_sense project.

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
from home import views as h
from about import views as a
from dashboard import views as d
from news import views as n
from user import views as u


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', h.homepage,name="home"), 
    path('signup/', u.signup),
    path('login/', u.login), 
    path('abouthsense/', a.aboutus),
    path('contract/', a.contract),
    path('developers/', a.developers), 
]