from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,View,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

# Create your views here.
class UserRegisterView(CreateView):
    model = User 
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'
    

class UserProfileView(View):
    
    def get(self, request):

        return render(request, 'profile.html')
    
    

class ProfileUpdateView(UpdateView):
    model = User 
    fields = ['first_name','last_name', 'email']
    template_name = 'profile_form.html'
    success_url = reverse_lazy('accounts:profile')
