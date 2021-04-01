from django.urls import path

from . import views

app_name = 'iotapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('process_a_guest', views.process_a_guest),
]
