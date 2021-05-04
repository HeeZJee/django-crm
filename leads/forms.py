from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm, UsernameField
from leads.models import Lead
from django.contrib.auth import get_user_model


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "last_name",
            "age",
            "agent",
        )

class LeadForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    age = forms.IntegerField(min_value=0)
    
    
User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ("username",)
            field_classes = {'username': UsernameField}