from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm,
)


class UserPasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('Current password'))

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('New password'),
        help_text=_('<small class="form-text text-muted">'
                    'Your password can’t be too similar to your other personal information.<br>'
                    'Your password must contain at least 8 characters.<br>'
                    'Your password can’t be a commonly used password.<br>'
                    'Your password can’t be entirely numeric.'
                    '</small>'))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('New password confirmation'))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('New Password'),
        help_text=_('<small class="form-text text-muted">'
                    'Your password can’t be too similar to your other personal information.<br>'
                    'Your password must contain at least 8 characters.<br>'
                    'Your password can’t be a commonly used password.<br>'
                    'Your password can’t be entirely numeric.'
                    '</small>'))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('New password confirmation'))

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Enter email'),
    }), help_text=_('<small class="form-text text-muted">Enter a valid email address.</small>'))

    class Meta:
        model = User
        fields = ['email']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Username'),
    }), required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('Password'), required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Enter email'),
    }), help_text=_('<small class="form-text text-muted">Enter a valid email address.</small>'))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Enter username'),
    }), help_text=_('<small class="form-text text-muted">Required. 150 characters or fewer. '
                    'Letters, digits and @/./+/-/_ only.</small>'))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('Password'),
        help_text=_('<small class="form-text text-muted">'
                    'Your password can’t be too similar to your other personal information.<br>'
                    'Your password must contain at least 8 characters.<br>'
                    'Your password can’t be a commonly used password.<br>'
                    'Your password can’t be entirely numeric.'
                    '</small>'))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }), label=_('Password confirmation'), help_text=_('<small class="form-text text-muted">'
                                                   'Enter the same password as before, for verification.'
                                                   '</small>'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('First name'),
    }), required=False, label=_('First name'),)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Last name'),
    }), required=False, label=_('Last name'),)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'placeholder': _('Birthday'),
    }), required=False, label=_('Birthday'),)

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-file',
    }), label=_('Profile Image'), required=False)

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'image']
