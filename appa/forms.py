from django import 	forms
from appa.models import RegistrationForm,Post

class Register(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields = ('FirstName', 'LastName', 'Email', 'Password','DOB','Skill','Experience','image',)	
		widgets={
		'Password':forms.PasswordInput(),
		}


class Login(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields=('Email','Password',)
		widgets={
		'Password':forms.PasswordInput(),
		}

class Search(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields=('FirstName','LastName',)

class Posts(forms.ModelForm):
	class Meta:
		model=Post
		fields=('user','posts_text',)


		