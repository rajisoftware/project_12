from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('raji/',raji,name='raji'),
    path('sudha/',sudha,name='sudha'),
]