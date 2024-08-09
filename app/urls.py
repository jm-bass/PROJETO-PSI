from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('atletas/', views.atletas, name="atletas"),
    path('sobre/', views.sobre, name="sobre"),
]