from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('updateTask/<str:pk>', views.updateTask, name="updateTask"),
    path('deleteTask/<str:pk>', views.deleteTask, name="deleteTask"),
    path("", views.landingPage, name="landingPage")
]
