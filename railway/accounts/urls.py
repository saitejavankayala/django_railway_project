from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'registration/$', views.registration, name='registration'),
    path(r'login/$', views.login.as_view(), name='login'),
    path(r'logout/$', views.logout, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
