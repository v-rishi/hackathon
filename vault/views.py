from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, View

from.forms import UserSignupForm, CreatePasswordForm
from .models import UserSavedPassword
# Create your views here.

class HomePageView(LoginRequiredMixin ,ListView):
    template_name = 'vault/home_page.html'
    
    def get_queryset(self):
        return UserSavedPassword.objects.filter(user = self.request.user)
    

class SignUpView(CreateView):
    form_class = UserSignupForm
    template_name = 'vault/signup.html'
    success_url = reverse_lazy('vault:login_view')
    

class CreatePasswordView(LoginRequiredMixin, CreateView):
    template_name='vault/create_password.html'
    form_class = CreatePasswordForm
    success_url = reverse_lazy('vault:home_page_view')
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
