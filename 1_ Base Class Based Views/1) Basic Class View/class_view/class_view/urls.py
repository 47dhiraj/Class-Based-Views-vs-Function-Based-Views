"""class_view URL Configuration

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

from class_view_app import views            # class_view_app vannale app ko name(i.e app ko name batw views.py lai import gareko vanne bujincha)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('parentclass1/', views.MyView.as_view(name='Ram'), name='parentclass1'),          # yedi views.py ko class ma kei variable ko value pathauna cha vani yesari url batw pani pathauna sakincha but, yo variable chai tyo class ma pahilai declare gareko huna parcha
    path('parentclass1/', views.MyView.as_view(), name='parentclass1'),

    path('childclass1/', views.MyViewChild.as_view(), name='childclass1'),

    path('home/', views.HomeClassView.as_view(), name='home'),

    path('about/', views.AboutClassView.as_view(), name='about'),

    path('contact/', views.ContactClassView.as_view(), name='contact'),


    # yo dubai url ko same view xa, template alag cha... yesari same view bata nai alag alag template dekhauna cha vani yesari garna sakincha
    path('info1/', views.InfoClassView.as_view(template_name='class_view_app/info1.html'), name='info1/'),
    path('info2/', views.InfoClassView.as_view(template_name='class_view_app/info2.html'), name='info2/'),
]
