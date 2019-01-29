from django.urls import path
from members import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("event/<int:pk>", views.EventDetailView.as_view(), name="event"),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('hello/<name>', views.hello_there, name='hello_there'),
]
