from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/$', views.index),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/(?P<user_id>\d+)/destroy/$', views.destroy),
    url(r'^users/(?P<user_id>\d+)/edit/$', views.edit),
    url(r'^users/add/$', views.add),
    url(r'^users/update/$', views.update),
    url(r'^users/create/$', views.create)
]
