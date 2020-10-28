from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from budget import models


'''class CustomerUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=['username','email','password']
		widgets = {
		'password': forms.PasswordInput(),
		}     
'''
class editprofile(UserChangeForm):

	class Meta:
		model=User
		fields=['username','email']




class CustomerUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	class Meta:
		model=User
		fields=['first_name','last_name','email','username','password']
		widgets = {
		'password': forms.PasswordInput()
		}
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile']