from django import forms
from myapp.models import Category, Institution, Donation
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'


class DonationForm(forms.ModelForm):
    user = forms.ModelChoiceField(required=False, queryset=User.objects.all())

    class Meta:
        model = Donation
        fields = '__all__'
