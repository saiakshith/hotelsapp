from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.contrib.auth.forms import UsernameField, AuthenticationForm
# create forms here

class CustomUCF(UserCreationForm):
  password1 = forms.CharField(
      label=_("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                        'placeholder': 'password',
                                        'class': 'form-control'}),
      help_text=password_validation.password_validators_help_text_html(),
  )
  password2 = forms.CharField(
      label=_("Password confirmation"),
      widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                        'placeholder': 're-enter password',
                                        'class': 'form-control'}),
      strip=False,
      help_text=_("Enter the same password as before, for verification."),
  )

  class Meta:
    model = User
    fields = ("username",)
    field_classes = {'username': UsernameField}
    widgets = {'username': forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'})}
      

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                         'placeholder': 'username',
                                                         'class': 'form-control'}))
  password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                           'placeholder': 'password',
                                          'class': 'form-control'}),
  )
