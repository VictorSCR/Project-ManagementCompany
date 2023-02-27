from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView



from users.forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('base')

    def get_user_context(self, title):
        pass


class UserLoginView(LoginView):
    from_class = AuthenticationForm
    template_name = 'users/login_form.html'

    def get_success_url(self):
        return reverse_lazy('base')


class UserLogoutView(LogoutView):
    pass


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)


class UserTemplateView(TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        return context
