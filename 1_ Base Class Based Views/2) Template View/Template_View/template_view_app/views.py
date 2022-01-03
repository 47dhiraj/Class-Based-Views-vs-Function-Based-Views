from django.shortcuts import render

from django.views.generic.base import TemplateView


# yedi context napathai garna cha vani yesari garni
# class HomeTemplateView(TemplateView):       # yo HomeTemplateView hamile banayeko view  le django ko TemplateView class lai inherit gareko cha
#     template_name = 'template_view_app/home.html'



# Yedi view batw template render garauda kheri context pani pathayera garna cha vani yesari garna sakincha
class HomeTemplateView(TemplateView):       # yo HomeTemplateView hamile banayeko view  le django ko TemplateView class lai inherit gareko cha
    template_name = 'template_view_app/home.html'
    
    
    def get_context_data(self, **kwargs):               # url batw j data aaucha tyo chai yo line ko **kwargs (i.e keyword arguments) ma aaccha
        print(kwargs)                   #url ko parameter ko value kwargs ma aaucha
        
        context = super().get_context_data(**kwargs)            #yo line call garnai parcha... i.e parent class lai call gareko
        

        # context ={ 'name' : 'Ram', 'course': '', 'roll' : 7, 'age' : 26 }             # yesari dictionary banayera pass garyo vanni extra context lai pass garna sakinna
        # print(context)

        context['name'] = 'Ram'               # yedi extra context lai pani pass garna cha vani yesari context banayera pass garna parcha
        context['roll'] = 7
        context['age'] = 26  
        print(context)

        
        return context
















