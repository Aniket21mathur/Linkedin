from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from appa.forms import SignUpForm,Login,Search,Posts,Comments
from appa.models import RegistrationForm,Post
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.conf import settings



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
            return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
            
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
			return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
		        
		else:
			return HttpResponse('invalid response')
	else:
		form=Login()
			
	return render(request,'html/login.html',{'form':form})		



def search(request):
	if request.method =='POST':
		form=Search(request.POST)
		if form.is_valid():
			userObj=form.cleaned_data
			try:
				searchuser=User.objects.get(username=request.POST['username'])
			except User.DoesNotExist:				
				searchuser=None
					
			if(searchuser is not None ):
				return render(request,'html/main.html',{'user':searchuser})
			else:
				return HttpResponse('user not found')
				
			
		else:
			return HttpResponse('enter a proper name to search')
	else:
		form=Search()


	return render(request,'html/search.html',{'form':form})	


def logout(request):
	auth_logout(request)
	return render(request,'html/logout.html')

def profilepage(request):
	return render(request,'html/main.html',{'user':request.user})




def posts(request):
	if request.user.is_authenticated:
		post_list=Post.objects.all()
		if request.method =='POST':
			form=Posts(request.POST)
			if form.is_valid():

				forma=form.save(commit=False)
				forma.user=request.user
				forma.save()
				
			
			else:
				return HttpResponse('fill the entries properly')
		else:
			form=Posts()


		return render(request,'html/posts.html',{'form':form,'post_list':post_list,})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))

def comment(request):
	if request.user.is_authenticated:

		if request.method=='POST':
			form=Comments(request.POST)
			if form.is_valid():

				
				formb=form.save(commit=False)
				formb.username_text=request.user
				formb.save()
				
				
			
			else:
				return HttpResponse('fill the entries properly')
		else:
			form=Comments()


		return render(request,'html/comment.html',{'form':form})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))


		



	











	



				

					
					
				

				
				





	








		
