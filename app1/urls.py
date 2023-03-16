from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('lava/',lava,name='lava'),
    path('kusha/',kusha,name='kusha'),
]