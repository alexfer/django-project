from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views

from users.forms import UserLoginForm, UserPasswordResetForm

urlpatterns = [
    path('accounts/profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name="users/login.html",
        authentication_form=UserLoginForm),
         name='login'
         ),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html',
        form_class=UserPasswordResetForm),
         name='password_reset'
         ),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
