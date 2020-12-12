from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms


# Create your views here.
from authentication.form import UserCreationAddForm


class RegisterView(views.CreateView):
    form_class = UserCreationAddForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')


class LogInView(auth_views.LoginView):
    template_name = 'auth/login.html'


class LogOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


