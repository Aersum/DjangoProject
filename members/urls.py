from django.urls import path
from members import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("event/<int:pk>", views.EventDetailView.as_view(), name="event"),
]
