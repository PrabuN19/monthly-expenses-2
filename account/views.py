from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.models import Group
from . import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from django.urls import reverse_lazy


'''
def signin(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		password1=request.POST['password1']
		password2=request.POST['password2']
		email=request.POST['email']
		if password1==password2:
			if User.objects.filter(username=username).exists():

				messages.info(request,'username taken')
				return redirect('signin')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'password taken')
				return redirect('signin')
			else:
			    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
			    user.save()
			    customer.user=user
			    customer.save()
			    my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
			    my_customer_group[0].user_set.add(user)
		return redirect('login')

	else:	
		return render(request,'registeration.html')
'''
'''def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    mydict={'userForm':userForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        
        if userForm.is_valid():
        	user=userForm.save()
        	user.set_password(user.password)
        	user.save()
        	my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
        	my_customer_group[0].user_set.add(user)
        	return HttpResponseRedirect('login')
        else:
        	messages.warning(request, 'Username or Email already used!')
        	return HttpResponseRedirect('signup')
    return render(request,'customersignup.html',context=mydict)'''


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
    	userForm=forms.CustomerUserForm(request.POST)
    	customerForm=forms.CustomerForm(request.POST,request.FILES)
    	if userForm.is_valid() and customerForm.is_valid():
    		user=userForm.save()
    		user.set_password(user.password)
    		user.save()
    		customer=customerForm.save(commit=False)
    		customer.user=user
    		customer.save()
    		my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
    		my_customer_group[0].user_set.add(user)
    		return HttpResponseRedirect('login')
    	else:
    		messages.warning(request, 'Username or Email already used!')
    		return HttpResponseRedirect('signup')
    return render(request,'customersignuptwo.html',context=mydict)




def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		try:
			user=auth.authenticate(username=User.objects.get(email=username),password=password)
		except:
			user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'invalid password or username')
			return redirect('login')
	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')



'''def edit_profile(request):
	if request.method=='POST':
		form=forms.editprofile(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form=forms.editprofile(instance=request.user)
		args={'form':form}
		return render(request,'edit_profile.html',args)'''

def edit_profile(request):
	context={}
	if request.method=='POST':
		username=request.POST['username']
		email=request.POST['email']

		usr=User.objects.get(id=request.user.id)
		usr.username=username
		usr.email=email
		usr.save()

		context['status']='change saved successfully'
	return render(request,'edit_profile.html',context)


def changepassword(request):
	context={}
	if request.method=='POST':
		crp=request.POST['crp']
		pas=request.POST['pas']
		cpass=request.POST['cpass']

		usr=User.objects.get(id=request.user.id)
		check=usr.check_password(crp)
		if check==True:
			if pas==cpass:
				usr.set_password(pas)
				usr.save()
				return redirect('/')

			else:
				context['text']='password not equal to confirm password'
		else:
			context['a']='current password not correct!'


	return render(request,'changepas.html',context)
