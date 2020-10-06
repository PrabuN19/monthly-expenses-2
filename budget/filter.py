import django_filters

from .models import *

class itemfilter(django_filters.FilterSet):
	class Meta:
		model=item
		fields=[
		    'itemname',
		    'title',
		    'date',
		    'price'
		]