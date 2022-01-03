from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView              # DetailView lai yesari import garna parcha
# Create your views here.


class StudentDetailView(DetailView):                # StudentDetailView is inhereting from DetailView
    model = Student

    # For Customizing DetailView.
    # template_name = 'App_DetailView/student.html'   # If you want to give your own customized template name the we will use 'template_name' attributes
                                                      # Yesle by default lini template name vaneko 'student_detail.html' i.e (modelname_detail.html)
                                                      # ListView ma jastai yaha DetailView ma vaney template_name change vayesakey pachi pani  'student_detail.html' lai auto recognize chai gardaina.                                                  
                                                      # So we need to change the template name what's given here.

    # context_object_name = 'stu'                      # template ma pass garni context name ho.
                                                       # Jun context name yeta diyeko cha tei context name template ma use garna parcha.

    # pk_url_kwarg = 'id'                              # urls.py ma use gareko <int:pk> ko thau ma yedi aru parameter variable dina man cha vani we can use 'pk_url_kwarg' attribute  (i.e :  pk_url_kwarg = 'variable')


    # This method is used to pass context to templates
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context['all_students'] = self.model.objects.all().order_by('name')     # Query lagayera sabai students ko record taneko ani 'all_students' as a context send gareko templates ma.
        return context
