from django.conf.urls import include,url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about-us/$', views.about_us, name='about_us'),
	url(r'^members/$', views.members, name='members'),
	url(r'^achievements/$', views.achievements, name='achievements'),
	url(r'^projects/$', views.our_projects, name='our_projects'),
	url(r'^tutorials/$', views.tutorials, name='tutorials'),
	url(r'^support-us/$', views.support_us, name='support_us'),
	url(r'^members/alumni/$', views.alumni, name='alumni'),
	url(r'^members/active/$', views.active_members, name='active_members'),
	url(r'^projects/ongoing/$', views.ongoing_projects, name='ongoing_projects'),
	url(r'^projects/completed/$', views.completed_projects, name='completed_projects'),

]