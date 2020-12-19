from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views


# Create your views here.
from architects.authentication.form import UserCreationAddForm


class RegisterView(views.CreateView):
    """Register user view"""
    form_class = UserCreationAddForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')


class LogInView(auth_views.LoginView):
    """Login view"""
    template_name = 'auth/login.html'


class LogOutView(auth_views.LogoutView):
    """logout view"""
    next_page = reverse_lazy('index')


