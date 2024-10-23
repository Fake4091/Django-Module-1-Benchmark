"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import string_times_view, count_hi_view, count_code_view

urlpatterns = [
    path('Warmup-2/String-times/<str:string>/<int:n>', string_times_view, name="string-times"),
    path('String-2/count_hi/<str:string>', count_hi_view, name="count-hi"),
    path('String-2/count-code/<str:string>', count_code_view, name="count-code"),
]
