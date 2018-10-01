from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.create,name='create'),
    url(r'saveContact$',views.saveContact,name='saveContact'),
]