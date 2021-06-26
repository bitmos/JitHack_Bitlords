
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signin/',views.singIN,name='signin'),
    path('postsign/',views.postsign),
   # path('post/',views.post),
    path('logout/',views.logout,name='log'),
    path('signup/',views.singUP, name='signup'),
    path('postsignup/',views.postsignup, name='postsignup'),
    path('create/',views.create, name='create'),
    path('post_create/',views.post_create, name='post_create'),
    path('check/',views.check, name='check'),
    path('post_check/',views.post_check, name='post_check'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)