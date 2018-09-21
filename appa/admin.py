from django.contrib import admin

# Register your models here.
from appa.models import RegistrationForm
from appa.models import MyNetwork
from appa.models import Job
from appa.models import Post



admin.site.register(RegistrationForm)
admin.site.register(MyNetwork)
admin.site.register(Job)
admin.site.register(Post)

