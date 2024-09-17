from django import forms
from django.utils.translation import gettext_lazy as _
from modules.comment.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Enter message'),
    }), label=_('Message'), required=True,)

    class Meta:
        model = Comment
        fields = ('comment',)
