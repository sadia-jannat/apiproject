#request and respone ar urls.py here
from django.urls import path
from firstapiproject import views

#weather project ar urls.py
from django.urls import path
from . import views

urlpatterns = [
   #request and respons ar code and see thunder client/local server all data
    path('api_list/', views.api_list),
    path('api_detail/<int:pk>/', views.api_detail),
    
    #weather project ar path
    path('', views.index),
    
]