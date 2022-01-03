"""Redirect_View URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from redirect_view_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', views.TemplateView.as_view(template_name='redirect_view_app/home.html'), name='blankhome'),

    # REDIRECTING TO URL
    # # yesari home/  or  index/  lekhera url ma hane pani teslai  / (i.e root) url mai redirect garni kaam RedirectView.as_view() le garcha
    # path('home/', views.RedirectView.as_view(url='/'), name='home'),        #yesari redirect garnu ko faida vaneko, kasaile home/ garyo vani pani home page mai jancha & url ma /home vanera display hudaina
    # path('index/', views.RedirectView.as_view(url='/'), name='index'),      #yesari redirect garnu ko faida vaneko, kasaile index/ garyo vani pani home page mai jancha & url ma /index vanera display hudaina

    #REDIRECTING TO PATTERN NAME
    # 1) Without URL parameter
    # yesari home/  or  index/  lekhera url ma hane pani teslai  diyeko pattern_name mai redirect garni kaam pani RedirectView.as_view() le garcha
    #path('home/', views.RedirectView.as_view(pattern_name='blankhome'), name='index'),

    # 2) With URL parameter
    # path('home/<int:id>/', views.HomeView.as_view(), name='home'),
    # path('profile/<int:id>/', views.TemplateView.as_view(template_name='redirect_view_app/home.html'), name='profile'),

    # ADVANCE way of Redirecting(in view of views.py page)
    path('home/<int:id>/', views.HomeView.as_view(), name='home'),
    path('profile/<int:id>/', views.TemplateView.as_view(template_name='redirect_view_app/home.html'), name='profile'),

]
