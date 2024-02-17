from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "second_name", "email", "phone", "text"]

class TaskForm(forms.Form):
    s = forms.FloatField(label="Площадь", min_value=0)
    r = forms.FloatField(label="Радиус", min_value=0)
    k = forms.FloatField(label="Проход", min_value=0)