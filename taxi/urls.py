from django.conf.urls import url, include
from taxi import views

urlpatterns = [
    url(r'^$', views.car_list, name='car_list'),
]
