from django import forms
from .models import Survey

BUSINESS_CHOICES = [
    ('restaurant', 'Общепит'),
    ('retail', 'Ритейл'),
    ('services', 'Услуги'),
]


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['answers']


class InstitutionForm(forms.Form):
    name = forms.CharField(label='Название заведения', max_length=100)
    city_country = forms.CharField(label='Страна и город', max_length=100)
    address = forms.CharField(label='Адрес', max_length=200)


class BusinessForm(forms.Form):
    business_type = forms.ChoiceField(choices=BUSINESS_CHOICES)
