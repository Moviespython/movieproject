from django.contrib.admin import views
from django.urls import path
from . import views

urlpatterns = [

   path('', views.index,name='index'),
   path('movie/<int:movie_id>/',views.detail,name='detail')
]