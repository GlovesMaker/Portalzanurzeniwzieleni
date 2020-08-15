from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
        url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	
]

