from django.urls import path
from emails import views

urlpatterns = [
    path('send/', views.send),
]
