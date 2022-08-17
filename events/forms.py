from .models import Application
from django import forms


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('firstname', 'lastname', 'phone', 'email', 'qualification', 'course', 'aboutus',)
        exclude = ('applied',)
