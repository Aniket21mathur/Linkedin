from django import forms
from appa.models import RegistrationForm

class RegistrationForm(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields=('FirstName','LastName','Email','Password','DOB','Skill','Experience','image')
		widgets={
		'Password':forms.PasswordInput(),
		}