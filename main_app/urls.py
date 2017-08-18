from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^treasure/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post_treasure/$', views.post, name='post'),
]