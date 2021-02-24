from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("Name needs to start with z")



class FormName(forms.Form):
    #name = forms.CharField(validators=[check_for_z]) # Validating with
    name = forms.CharField()
    email = forms.EmailField()
    confirm_email = forms.EmailField(label='Enter your emailagain')
    text = forms.CharField(widget=forms.Textarea)
    #botcatcher = forms.CharField(widget=forms.HiddenInput,required=False,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        cnf_email = all_clean_data['confirm_email']

        if email!=cnf_email:
            raise forms.ValidationError("Email and Confirm-email should be same")