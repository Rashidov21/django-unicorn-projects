from django.shortcuts import render
from django.views.generic import CreateView,View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserRegisterView(CreateView):
    model = User 
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'
    

class UserProfileView(View):
    
    def get(self, request):
        return render(request, '')