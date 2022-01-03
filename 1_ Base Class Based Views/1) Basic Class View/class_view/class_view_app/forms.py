from django import forms     # django batw forms lai import garna parcha

class ContactForm(forms.Form):              # hamile banako form class ko name ContactForm rakheko
    name = forms.CharField(max_length=70)       # name chai form ko field name ho