from django.shortcuts import render
from django.views.generic import TemplateView
from appa.forms import Register,Login,Search
from appa.models import RegistrationForm
from django.http import HttpResponse
from django import forms

class firstview(TemplateView):
	template_name='html/home.html'
	def homeview(self,request):
		return render(request,'html/home.html')

def register(request):
	if request.method == 'POST':
		form=Register(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			email=userObj['Email']
			password=userObj['Password']
			if not(RegistrationForm.objects.filter(Email=email).exists() or RegistrationForm.objects.filter(Password=password)):
				form.save()
			else:
				 return HttpResponse('Looks like a username with that email or password already exists')
				
		else:
			return HttpResponse('fill the entries properly')
	else:
		form=Register()
	return render(request,'html/register.html',{'form':form})


def login(request):
	if request.method =='POST':
		form=Login(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			try:

				user=RegistrationForm.objects.get(Email=request.POST['Email'])
				password=RegistrationForm.objects.get(Password=request.POST['Password'])


			except RegistrationForm.DoesNotExist:
				user=None
				password=None	
			if(user is not None and password is not None and request.POST['Password']==user.Password ):
				return render(request,'html/main.html',{'user':user})
			else:
				return HttpResponse('invalid email or password')
				
			
		else:
			return HttpResponse('fill the entries properly')
	else:
		form=Login()


	return render(request,'html/login.html',{'form':form})	


def search(request):
	if request.method =='POST':
		form=Search(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			try:
				user=RegistrationForm.objects.get(FirstName=request.POST['FirstName'])
			except RegistrationForm.DoesNotExist:				
				user=None
					
			if(user is not None and request.POST['LastName']==user.LastName ):
				return render(request,'html/main.html',{'user':user})
			else:
				return HttpResponse('user not found')
				
			
		else:
			return HttpResponse('enter a proper name to search')
	else:
		form=Search()


	return render(request,'html/search.html',{'form':form})	
	



				

					
					
				

				
				





	








		
