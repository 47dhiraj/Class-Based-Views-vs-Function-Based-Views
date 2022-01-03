from django.shortcuts import render

from django.views.generic.base import TemplateView, RedirectView


class HomeView(RedirectView):
    pattern_name = 'profile'
    permanent = True
    query_string = True             #by default url ma query string display hudaina (i.e False huncha),, yedi query string lai url ma display garauna cha vani TRUE garna parcha


    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)










