from django import 	forms
from appa.models import RegistrationForm

class Register(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields = ('FirstName', 'LastName', 'Email', 'Password','DOB','Skill','Experience','image',)	


class Login(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields=('Email','Password',)

class Search(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields=('FirstName','LastName',)
		