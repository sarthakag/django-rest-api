from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ride/',views.data,name='data'),
    url(r'rides/(?P<id>\d+)/$',views.getdatabyId,name='getdatabyId')
]