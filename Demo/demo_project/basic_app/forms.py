from django import forms
from basic_app.models import UserProfile

class UserProfileForm(forms.ModelForm):
      class Meta:
          model = UserProfile
          fields = '__all__'