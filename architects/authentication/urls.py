from django.urls import path

from authentication.views import LogInView, RegisterView, LogOutView

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
]

from .receivers import *