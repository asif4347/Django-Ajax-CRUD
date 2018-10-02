
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from Books.views import BookViewSet

router=routers.DefaultRouter()
router.register(r'books-api',BookViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'ajax/',include('contact.urls')),
    url(r'books/',include('Books.urls')),
    url(r'api/',include(router.urls)),

]
