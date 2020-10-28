from django.shortcuts import  redirect,render,get_object_or_404
from .models import months,item,Customer
from django.utils.text import slugify
from .form import priceform
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .filter import itemfilter
from django.contrib import messages



def index(request):
	return render(request,'index.html')


def detail(request,months_slug):
	month=get_object_or_404(months,slug=months_slug)
	context={}
	if request.method=='GET':
		customer=Customer.objects.get(user_id=request.user.id)
		items=month.item.all().filter(customer_id = customer)
	   
		myfilter=itemfilter(request.GET, queryset=items)
		items=myfilter.qs

		return render(request,'detail.html',{'month':month,'myfilter':myfilter,'items':items,})

	elif request.method=='POST':
		form=priceform(request.POST)
		if form.is_valid():
			itemname=form.cleaned_data['itemname']
			title=form.cleaned_data['title']
			price=form.cleaned_data['price']
			date=form.cleaned_data['date']

			item.objects.create(
				month=month,
				itemname=itemname,
				customer=Customer.objects.get(user_id=request.user.id),
				title=title,
				price=price,
				date=date,
				).save()
	return HttpResponseRedirect(months_slug)


class projectcreateview(CreateView):
	model=months
	template_name='list1.html'
	fields=['name']

	def get_success_url(self):
		return slugify(self.request.POST['name'])


	def form_valid(self,form):
		self.object=form.save(commit=False)
		form.instance.customer = Customer.objects.get(user_id=self.request.user.id)
		self.object.save()
		return HttpResponseRedirect(self.get_success_url())
	'''def form_invalid(self,form):
		return render(self.request,self.template_name)'''

@login_required(login_url='account/login')		
def my(request):
	customer=Customer.objects.all().get(user_id=request.user.id)
	month=months.objects.all().filter(customer_id=customer)
	return render(request,'list.html',{'month':month})



def delete(request,id):
	it=item.objects.get(id=id)
	it.delete()
	return redirect('mylist')
	
 


def month_del(request,id):
	mon=months.objects.get(id=id)
	mon.delete()
	return redirect('mylist')



