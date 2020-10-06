from django import forms


class priceform(forms.Form):
	itemname=forms.CharField()
	title=forms.CharField()
	price=forms.IntegerField()
	date=forms.DateField()