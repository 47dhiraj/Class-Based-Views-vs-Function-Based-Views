from django.shortcuts import render
from django.views.generic.list import ListView          #ListView lai yesari import garna parcha
from .models import  Student                    #Student model lai import gareko

# Create your views here.
class StudentList(ListView):
    model = Student     # This Single line will perform all below task automatically in Generic ListView:
                        # student = Student.object.all()
                        # context = {'student_list': student}           # yedi ListView use gari rako cha vani, django template ma data pathauda key ko name by default 'modelname_list' rakhcha
                        # return render(request, 'App_ListView/student_list.html', context)
################################## CUSTOMIZING Generic ListView #####################################################

    #give your own template name (yedi tmlai modelname_list.html ko format ma html file lai name rakhnu chaina vani)
    template_name = 'App_ListView/student.html'  # If this is not kept then we have to give default template name as 'student_list.html' 
                                                 # i.e(moedl_list.html) Model name in small. 
                                                 # '_list' is suffix for template in Generic ListView.
                                                 # To give different name to template as compared to default template name we have given this 
                                                 #'template_name' attribute.

    # ordering = ['name']         #If you want to order all the records by it's name 
    # ordering = ['roll']         #If you want to order all the records by it's roll no. 

    #give your custom+ context key
    # context_object_name = 'mystudents'       # provides  our own context object name which can be used in templates.
                                               # If this is not used then our default context object name will be 'student_list' i.e(modelname_list)


    #Filter all records queryset as per your needs
    # def get_queryset(self):               
        # return Student.objects.filter(course='PHP')   


    # If you want to pass the context from Generic ListView 
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, *kwargs)
        context['order_by'] = Student.objects.all().order_by('name')
        return context




    # To render different templates depending upon the condition
    #def get_template_names(self):                      # django ko Generic ListView le provide gareko method ho
    #    if self.request.COOKIES['user'] == 'sonam':    # If  'user' vanni cookie ko value ma name 'sonam' cha vani sonam.html template render huncha.
                                                        # Cookie value and name has to be set manually by going into browser developer tool.
    #       template_name = 'App_ListView/sonam.html'   # template_name mathidefine gareko attributes ma sonam.html template haldeko.
    #    else:
    #       template_name = self.template_name          # If cookie ma name sonam chaina vani default template load garauni
    #                                                   # i.e in lin no. 14 ('App_ListView/student.html)
    #    return [template_name]                         # this function will return the list so 'template_name' is in type of list.

    


    # Another Real life example for 'get_template_name' method
    # def get_template_names(self):

    #     if self.request.user.is_superuser:              # If the user is logged in as 'superuser' then show the 'super.html' template
    #         template_name = 'App_ListView/super.html'
            
    #     elif self.request.user.is_staff:                # If the user is logged in as 'staff' then show the 'staff.html' template
    #         template_name = 'App_ListView/staff.html'

    #     else:                                            # If the user is logged in as normal user then show the 'student.html' template 
    #                                                      # i.e in line no. 16 ('App_ListView/student.html)
    #         template_name = self.template_name

    #     return [template_name]








