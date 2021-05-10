
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
'''from .views import index'''
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signin/',views.singIN,name='signin'),
    path('postsign/',views.postsign),
    path('logout/',views.logout,name='log'),
    path('signup/',views.singUP, name='signup'),
    path('postsignup/',views.postsignup, name='postsignup'),
    

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)