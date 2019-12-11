"""Mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from sign import views
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello),
    path('login', views.login),
    path('', views.login),
    # path('login_action', views.login_action),
    path('manage', views.manage),
    path('event_search', views.event_search),
    path('sign_index/<int:event_id>', views.sign_index),

    path('guest', views.guest),
    path('logout', views.logout),
]
