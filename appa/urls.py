from django.conf.urls import url
from appa import views as appa_views

urlpatterns = [


url(r'^$',appa_views.firstview.as_view(), name='home'),
url(r'^register/$',appa_views.register, name='reg'),
url(r'^login/$',appa_views.login, name='lgin'),


]