from django import forms
from website.models import Contact,newsletter
from captcha.fields import CaptchaField
class FORM_NAME(forms.Form):
    name=forms.CharField()
    subject=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea())



class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta():
        model=Contact
        fields='__all__'


class NewsletterForm(forms.ModelForm):
    class Meta():
        model=newsletter
        fields='__all__'