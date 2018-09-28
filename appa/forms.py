from django import 	forms
from appa.models import RegistrationForm,Post,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''class Register(forms.ModelForm):
	class Meta:
		model=RegistrationForm
		fields = ('FirstName', 'LastName', 'Email', 'Password','DOB','Skill','Experience','image',)	
		widgets={
		'Password':forms.PasswordInput(),
		}'''

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class Login(forms.ModelForm):
	class Meta:
		model=User
		fields=('username','password',)
		

class Search(forms.Form):
	username=forms.CharField(label='username')

class Posts(forms.ModelForm):
	class Meta:
		model=Post
		fields=('posts_text',)


class Comments(forms.ModelForm):
	class Meta:
		model=Comment
		fields=('post','comment_text',)



		