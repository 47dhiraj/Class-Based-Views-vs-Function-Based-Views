from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

from .forms import ContactForm      # forms.py page batw hamile banayeko ContactForm lai import gareko

#Class Based View

class MyView(View):             # MyView vanni class hamile banako class ho & this MyView class is inheriting from django view jun chai hamile import gareko chau
    name = 'Hari'               # class vitra yesari attribute pani declare garna sakincha...  url path batw yo attribute ko lagi value pani pathauna skincha... checkout path in ursl.py
    def get(self, request):
        # return HttpResponse('<h1>MyView class</h1>')
        return HttpResponse(self.name)


class MyViewChild(MyView):  
    # name = 'Madan'        # parent class(i.e MyView class) batw name attribute lai access garna pani sakincha, but yei child class ma parent class ko attribute lai override pani garna sakincha  
    def get(self, request):
        # return HttpResponse('<h1>MyViewChild class</h1>')
        return HttpResponse(self.name)


class HomeClassView(View):
    def get(self, request):
        return render(request, 'class_view_app/home.html')

class AboutClassView(View):
    def get(self, request):
        context = {'message': 'This is context message for About page'}         # yesari class based view batw template ma context pani pathauna sakincha
        return render(request, 'class_view_app/about.html', context)


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        context = {'form':form}
        return render(request, 'class_view_app/contact.html', context)


    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('<h4>Your form has be successfully submitted.</h4>')


class InfoClassView(View):
    # template_name = 'class_view_app/info.html'
    template_name = ''
    def get(self, request):
        context = {'info': 'This is information'}
        return render(request, self.template_name, context)









