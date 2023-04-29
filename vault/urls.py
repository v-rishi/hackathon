from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import CreatePasswordView, HomePageView, SignUpView

app_name='vault'

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page_view'),
    path('signup/', SignUpView.as_view(), name='signup_view'),
    path('login/', LoginView.as_view(template_name='vault/login.html'), name='login_view'),
    path('logout/', LogoutView.as_view(template_name='vault/logout.html'), name='logout_view'),
    path('create/', CreatePasswordView.as_view(), name='create_password_view')
]