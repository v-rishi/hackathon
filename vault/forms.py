from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.forms import TextInput, ModelForm
from .models import UserSavedPassword

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        
        
class CreatePasswordForm(ModelForm):
    class Meta:
        model = UserSavedPassword
        fields = ['title', 'username','password']
    
    title = forms.CharField(label='Name')
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    
    # def save(self, commit=True):
    #     instance = super(CreatePasswordForm, self).save(commit=False)
    #     instance.user = self.request.user
    #     instance.save()
    #     return instance
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        

