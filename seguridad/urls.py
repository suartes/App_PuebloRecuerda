from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^login/$', views.authlogin, name = 'authlogin',),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name = 'logout',),
	url('', include('social.apps.django_app.urls', namespace='social')),
]