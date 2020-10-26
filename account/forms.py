from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class CustomerUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=['username','email','password']
		widgets = {
		'password': forms.PasswordInput(),
		}     

class editprofile(UserChangeForm):

	class Meta:
		model=User
		fields=['username','email']