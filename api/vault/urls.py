from django.urls import path 
from .views import GenerateRandomPasswordAPIView

app_name =  'api_vault'

urlpatterns = [ 
        path('generate_random_password/', GenerateRandomPasswordAPIView.as_view(), name='generate_random_password_api_view')
]