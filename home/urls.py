from django.conf.urls import url, include
from home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
