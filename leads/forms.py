from django import forms


class LeadForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    age = forms.IntegerField(min_value=0)