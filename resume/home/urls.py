
from django.urls import path
from home import views

urlpatterns = [
    path('',views.accept , name='index'),
    path('pdf',views.pdf_print,name='pdf'),
   
]