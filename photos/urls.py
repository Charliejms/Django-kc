from django.conf.urls import url
from django.contrib import admin

from photos.api import PhotoListAPI, PhotoDetailAPI
from users.views import LoginView, LogoutView

from photos.views import HomeView, PhotoDetailView, PhotoCreationView, PhotosListView

urlpatterns = [

    #Photo URLs
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^photo/(?P<pk>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^create$', PhotoCreationView.as_view(), name='photos_create'),
    url(r'^photos/$', PhotosListView.as_view(), name='photos_my_photos'),

    #API Photo URLs
    url(r'^api/1.0/photos/$', PhotoListAPI.as_view() , name='api_photos_list'),
    url(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view() , name='api_photos_detail'),
]
