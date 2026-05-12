from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="Home"),
    path('chat/', views.chat ,name="ChatBot"),
]
