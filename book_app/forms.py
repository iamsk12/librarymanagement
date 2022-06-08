from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    User._meta.get_field('email')._unique = True
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )