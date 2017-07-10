
from django.conf.urls import url

from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView


urlpatterns = [
    #  Web user URLs
    url(r'^login$', LoginView.as_view(), name='user_login'),
    url(r'^logout$', LogoutView.as_view(), name='user_logout'),

    #  API user URLs
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='api_user_detail')
]
