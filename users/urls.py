from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]