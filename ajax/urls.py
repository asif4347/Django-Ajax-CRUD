
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'ajax/',include('contact.urls')),
    url(r'books/',include('Books.urls')),

]
