from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from content.models import Entry
from comment.models import Comment
from base.tools import sendmail


# Create your views here.

def comment(request, id):
    try:
        entry = Entry.objects.get(id=id)
    except (Entry.DoesNotExist):
        return render(request, 'errors/404.html', status=404)

    url = request.META.get('HTTP_REFERER')

    if not request.POST['author'] or not request.POST['message'] or not request.POST['email']:
        messages.error(request, _('All fields cannot be empty.'), extra_tags='alert alert-danger')
    else:

        if not request.user.is_authenticated:
            return redirect('login')

        email = request.POST['email']
        author = request.POST['author']
        try:
            validate_email(email)
            sendmail.send(
                email,
                'Mew Comment',
                'Posted new comment to {}'.format(url),
            )

            message = Comment(author=author, comment=request.POST['message'], approved=True)
            message.entry = entry
            message.save()

            messages.success(request, _('You message has been sent successfully.'), extra_tags='alert alert-success')

        except(ValidationError):
            messages.error(request, _('Invalid email address.'), extra_tags='alert alert-danger')

    return HttpResponseRedirect(url)
