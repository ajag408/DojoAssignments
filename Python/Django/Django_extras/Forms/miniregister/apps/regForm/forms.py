from django import forms
from .models import User
class RegisterForm(forms.ModelForm):
  class Meta:
      model = User
      fields = '__all__'
      widgets = {
        'password': forms.PasswordInput(),
        'confirm_password': forms.PasswordInput()
      }
