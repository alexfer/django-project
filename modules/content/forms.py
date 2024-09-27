from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Entry


class _CreateEntryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Enter entry title'),
    }), label=_('Title'), max_length=250)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Enter entry content'),
    }), label=_('Content'),)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-file',
    }), label=_('Entry image'), required=False)

    class Meta:
        model = Entry
        fields = ('title', 'content', 'image',)


class CreateEntryForm(_CreateEntryForm):

    def __init__(self, *args, **kwargs):
        super(_CreateEntryForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = _('<small class="form-text text-muted">This field is required</small>')
        self.fields['content'].help_text = _('<small class="form-text text-muted">This field is required</small>')


class _ChangeEntryForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
        required=True,
        label=_('Date'),
    )
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Enter entry title'),
    }), label=_('Title'), max_length=250)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Enter entry content'),
    }), label=_('Content'), )

    class Meta:
        model = Entry
        fields = ('created_at', 'title', 'content',)


class ChangeEntryForm(_ChangeEntryForm):
    def __init__(self, *args, **kwargs):
        super(_ChangeEntryForm, self).__init__(*args, **kwargs)
        self.fields['created_at'].help_text = _('<small class="form-text text-muted">This field is required. '
                                                'Date format should be YYYY-MM-DD HH:MM:SS</small>')
        self.fields['title'].help_text = _('<small class="form-text text-muted">This field is required</small>')
        self.fields['content'].help_text = _('<small class="form-text text-muted">This field is required</small>')
