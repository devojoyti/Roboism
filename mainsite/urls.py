from django.conf.urls import include,url
from . import views
import django.contrib.auth.views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about-us/$', views.about_us, name='about_us'),
	url(r'^members/$', views.members, name='members'),
	url(r'^achievements/$', views.achievements, name='achievements'),
	url(r'^projects/$', views.projects, name='projects'),
	url(r'^projects/completed/$', views.completed_projects, name='completed_projects'),
	url(r'^projects/ongoing/$', views.ongoing_projects, name='ongoing_projects'),
	url(r'^tutorials/$', views.tutorials, name='tutorials'),
	url(r'^contact/$', views.contact_us, name='contact_us'),
	url(r'^members/alumni/$', views.alumni, name='alumni'),
	url(r'^members/active/$', views.active_members, name='active_members'),
	url(r'^members/active/(\w+)/$', views.member_details, name='member_details'),
	url(r'^members/alumni/(\w+)/$', views.member_details, name='member_details'),
    url(r'^login/',auth_views.login, name="auth_views.login"),
    url(r'^home/', views.index, name='index'),
    url(r'^logout/$', views.logout_page),
    url(r'^register/$', views.register),
    url(r'^profile/$', views.userprofile, name='userprofile'),
    url(r'^profile/edit/$', views.editprofile, name='editprofile'),
    url(r'^register/success/$', views.success, name='success'),
    url(r'^register/fill_info/$', views.fill_info, name='fill_info'),
	url(r'^profile/addproject/$', views.addproject, name='addproject'),
	url(r'^profile/editproject/(\d+)/$', views.editproject, name='editproject'),
	url(r'^developers/$', views.developers, name="developers"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
