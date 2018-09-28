from django.conf.urls import url
from appa import views as appa_views

urlpatterns = [


url(r'^$',appa_views.firstview.as_view(), name='home'),
url(r'^register/$',appa_views.signup, name='reg'),
url(r'^login/$',appa_views.login, name='lgin'),
url(r'^login/search/$',appa_views.search, name='srch'),
url(r'^logout/$',appa_views.logout, name='lgout'),
url(r'^login/posts/$',appa_views.posts, name='pst'),
url(r'^login/comments/$',appa_views.comment, name='cmmt'),




]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)