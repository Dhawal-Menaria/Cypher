from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="Home"),
    path('chatbot/', views.home ,name="ChatBot"),
]
