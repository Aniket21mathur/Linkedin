from django.shortcuts import render
from django.views.generic import TemplateView
from appa.forms import SignUpForm,Login,Search,Posts,Comments
from appa.models import RegistrationForm,Post
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login as auth_login

class firstview(TemplateView):
	template_name='html/home.html'
	def homeview(self,request):
		return render(request,'html/home.html')


activeuser=None
searchuser=None

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            
    else:
        form = SignUpForm()
    return render(request, 'html/register.html', {'form': form})

'''def register(request):
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
	return render(request,'html/register.html',{'form':form})'''


'''def login(request):
	global activeuser
	if request.method =='POST':
		form=Login(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			try:

				activeuser=RegistrationForm.objects.get(Email=request.POST['Email'])
				password=RegistrationForm.objects.get(Password=request.POST['Password'])


			except RegistrationForm.DoesNotExist:
				activeuser=None
				password=None	
			if(activeuser is not None and password is not None and request.POST['Password']==activeuser.Password ):
				return render(request,'html/main.html',{'user':activeuser})
			else:
				return HttpResponse('invalid email or password')
				
			
		else:
			return HttpResponse('fill the entries properly')
	else:
		form=Login()


	return render(request,'html/login.html',{'form':form})	
	'''

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return HttpResponse('valid user')
        
		else:
			return HttpResponse('invalid response')
	else:
		form=Login()
			
	return render(request,'html/login.html',{'form':form})		



def search(request):
	global searchuser
	if request.method =='POST':
		form=Search(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			try:
				searchuser=RegistrationForm.objects.get(FirstName=request.POST['FirstName'])
			except RegistrationForm.DoesNotExist:				
				searchuser=None
					
			if(searchuser is not None and request.POST['LastName']==searchuser.LastName ):
				return render(request,'html/main.html',{'user':searchuser})
			else:
				return HttpResponse('user not found')
				
			
		else:
			return HttpResponse('enter a proper name to search')
	else:
		form=Search()


	return render(request,'html/search.html',{'form':form})	


def logout(request):
	global user
	user=None
	return render(request,'html/logout.html')


def posts(request):
	global activeuser
	post_list=Post.objects.all()
	if request.method =='POST':
		form=Posts(request.POST)
		if form.is_valid():

			form.save()
			
				
			
		else:
			return HttpResponse('fill the entries properly')
	else:
		form=Posts()


	return render(request,'html/posts.html',{'form':form,'post_list':post_list})


def comment(request):
	global activeuser
	if request.method=='POST':
		form=Comments(request.POST)
		if form.is_valid():

			form.save()
			
				
			
		else:
			return HttpResponse('fill the entries properly')
	else:
		form=Comments()


	return render(request,'html/comment.html',{'form':form})



	











	



				

					
					
				

				
				





	








		
