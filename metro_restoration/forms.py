from django import forms
from django.utils.translation import ugettext_lazy as _

class CustomContactForm(forms.Form):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={ "class": "form-control", "placeholder": "Your Name", "required": "required" }))
    phone = forms.CharField(label=_("Phone"), widget=forms.TextInput(attrs={ "class": "form-control", "type": "tel", "placeholder": "555-555-5555" }))
    email = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={ "class": "form-control", "type": "email", "placeholder": "you@domain.com", "required": "required" }))
    subject = forms.CharField(label=_("Subject"), required=False, widget=forms.TextInput(attrs={ "class": "form-control" }))
    content = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={ "class": "form-control", "required": "required" }))

    template = "cmsplugin_contact/contact.html"