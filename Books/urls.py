from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.book_list,name='book_list'),
    url(r'^create/$', views.book_create, name='book_create'),
    url(r'^(?P<pk>\d+)/book_update/$', views.book_update, name='book_update'),
    url(r'^(?P<pk>\d+)/book_delete/$', views.book_delete, name='book_delete'),



]