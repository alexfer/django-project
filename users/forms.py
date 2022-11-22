from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm
)


class UserPasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Current password')

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='New password',
        help_text='<small class="form-text text-muted">'
                  'Your password can’t be too similar to your other personal information.<br>'
                  'Your password must contain at least 8 characters.<br>'
                  'Your password can’t be a commonly used password.<br>'
                  'Your password can’t be entirely numeric.'
                  '</small>')

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='New password confirmation')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='New Password',
        help_text='<small class="form-text text-muted">'
                  'Your password can’t be too similar to your other personal information.<br>'
                  'Your password must contain at least 8 characters.<br>'
                  'Your password can’t be a commonly used password.<br>'
                  'Your password can’t be entirely numeric.'
                  '</small>')

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='New password confirmation')

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email',
    }), help_text='<small class="form-text text-muted">Enter a valid email address.</small>')

    class Meta:
        model = User
        fields = ['email']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }), required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Password', required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email',
    }), help_text='<small class="form-text text-muted">Enter a valid email address.</small>')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter username',
    }), help_text='<small class="form-text text-muted">Required. 150 characters or fewer. '
                  'Letters, digits and @/./+/-/_ only.</small>')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Password',
        help_text='<small class="form-text text-muted">'
                  'Your password can’t be too similar to your other personal information.<br>'
                  'Your password must contain at least 8 characters.<br>'
                  'Your password can’t be a commonly used password.<br>'
                  'Your password can’t be entirely numeric.'
                  '</small>')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label='Password confirmation', help_text='<small class="form-text text-muted">'
                                                 'Enter the same password as before, for verification.'
                                                 '</small>')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First name',
    }), required=False)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last name',
    }), required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'Birthday',
    }), required=False)

    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control-file',
    }), required=False)

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'image']
