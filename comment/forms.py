from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter message',
    }), label='Message', required=True,)

    class Meta:
        model = Comment
        fields = ('comment',)
