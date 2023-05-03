from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',views.UserRegisterView.as_view(), name='register'),
    path('profile/',views.UserProfileView.as_view(), name='profile'),
    
]
