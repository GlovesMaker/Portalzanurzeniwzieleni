from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^search/$', views.search, name='search'),
        url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        url(r'^contact/', views.contact, name='contact'),
	url(r'^cooperation/', views.cooperation, name='cooperation'),
        url(r'^worth_recommending/', views.worth_recommending, name='worth_recommending'),
]

