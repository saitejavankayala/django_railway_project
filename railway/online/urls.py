from django.urls import path

from . import views

urlpatterns = [
    path('online/alogin', views.alogin, name='alogin'),
    path('', views.index, name='index'),

    path('checkpoint', views.checkpoint, name='checkpoint'),
    path('end', views.end, name='end'),

    path('fill', views.fill, name='fill'),
    path('display', views.display, name='display'),

    path('online/train_list', views.train_list, name='train_list'),
    path('view/<int:pk>', views.train_view, name='train_view'),
    path('new', views.train_create, name='train_new'),
    path('edit/<int:pk>', views.train_update, name='train_edit'),
    path('delete/<int:pk>', views.train_delete, name='train_delete'),

]
