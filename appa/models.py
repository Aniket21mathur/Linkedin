from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(models.Model):
	FirstName=models.CharField(max_length=30)
	LastName=models.CharField(max_length=30)
	Email=models.EmailField(max_length=70)
	Password=models.CharField(max_length=30)
	DOB=models.DateField()
	Skill=models.CharField(max_length=200,default="Your skills")
	Experience=models.CharField(max_length=200,default="Your Experience")
	image=models.ImageField(upload_to='appa/templates/html/profile_image',blank=True)
	def __str__(self):
		return self.Email

		
class MyNetwork(models.Model):
	user=models.ForeignKey(RegistrationForm,on_delete=models.CASCADE)
	friends_text=models.CharField(max_length=200)
	def __str__(self):
		return self.friends_text

class Job(models.Model):
	user=models.ForeignKey(RegistrationForm,on_delete=models.CASCADE)
	jobs_text=models.CharField(max_length=200)
	def __str__(self):
		return self.jobs_text			

class Post(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	posts_text=models.CharField(max_length=200)
	def __str__(self):
		return self.posts_text				

class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	comment_text=models.CharField(max_length=200)
	username_text=models.CharField(max_length=32)
	def __str__(self):
		return self.comment_text		