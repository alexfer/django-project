from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _

from content.models import Entry
from comment.models import Comment


# Create your views here.

@login_required
def comment(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    url = request.META.get('HTTP_REFERER')

    if not request.POST['message']:
        messages.error(request, _('Field `message` cannot be empty.'), extra_tags='alert alert-danger')
    else:
        try:
            message = Comment(user_id=request.user.id, comment=request.POST['message'], approved=True)
            message.entry = entry
            message.user = request.user
            message.save()

            messages.success(
                request,
                _('You message has been published successfully.'),
                extra_tags='alert alert-success',
            )

        except ValidationError:
            messages.error(request, _('Invalid email address.'), extra_tags='alert alert-danger')

    return HttpResponseRedirect(url)
