from django import forms
from django.contrib.auth.models import User


class priceform(forms.Form):
	itemname=forms.CharField(required=True)
	title=forms.CharField(required=True)
	price=forms.IntegerField(required=True)
	date=forms.DateField(required=True)
