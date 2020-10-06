from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from  django.contrib import messages
from django.contrib.auth.models import Group
from . import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.views import LoginView,LogoutView

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
    return render(request,'customersignup.html',context=mydict)




def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'invalid password or username')
			return redirect('login')
	else:
		return render(request,'login.html')



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
        return HttpResponseRedirect('customerlogin')
    return render(request,'customersignup.html',context=mydict)



class customer_login_view(LoginView):
	template_name='customerlogin.html'
	def get_success_url(self):
		return redirect('/')
		'''
def logout(request):
	auth.logout(request)
	return redirect('/')