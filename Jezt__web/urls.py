"""Jezt__web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path('about-us/',views.about_us,name='about-us'),
    path('technology/',views.technology,name='technology'),
    path('chatbot/',views.Ai,name="chatbot"),
    path('clear-chat-history/', views.clear_chat_history, name='clear_chat_history'),
    path('contact-us/',views.request_callback, name='contact-us'),
    path('csv/', views.download_csv, name='download_csv'),
    path('try',views.trial, name='trial'),
]
