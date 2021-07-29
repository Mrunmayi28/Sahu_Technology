from django.contrib import admin
from django.urls import path,include
from home import views 

urlpatterns = [
    path('',views.accept , name='index.html'),
    path('list',views.lost , name='list.html')
]
    