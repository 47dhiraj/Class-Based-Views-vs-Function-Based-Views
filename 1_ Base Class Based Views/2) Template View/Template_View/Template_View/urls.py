"""Template_View URL Configuration

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

from template_view_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #yesari pani template lai template_name ma url batw view samma pass garna sakincha
    path('about/', views.TemplateView.as_view(template_name='template_view_app/about.html'), name='about'), #khyal gar yo line ko TemplateView chai by default django le diyeko view ho for rendering template



    # yesari aafno view banayera(i.e HomeTemplateView) pani sajilai template render garna sakincha
    # path('index/', views.HomeTemplateView.as_view(), name='home'),

    # yesari view ma, url batw nai pani extra context pani pass garna sakincha
    # path('index/', views.HomeTemplateView.as_view(extra_context={'course': 'BSC CSIT'}), name='home'),

    # yedi url batw parameter and both extra_context pathauna cha vani yesari pathauna sakincha
    path('index/<int:id>', views.HomeTemplateView.as_view(extra_context={'course': 'BSC CSIT'}), name='home'),
]
