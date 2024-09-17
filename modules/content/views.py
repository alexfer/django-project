from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from modules.comment.forms import CommentForm
from modules.content.models import Entry
from django.views.generic.list import ListView
from django.contrib import messages
from modules.comment.models import Comment
from django.utils.translation import gettext_lazy as _


def details(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    comments = Comment.objects.filter(entry_id=entry.id, approved=True).order_by('-created_at')

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.entry = entry
            comment.user = request.user
            comment.approved = True
            comment.save()

            messages.success(
                request,
                _('You message has been published successfully.'),
                extra_tags='alert alert-success',
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()

    context = {
        'entry': entry,
        'form': form,
        'comments': comments,
    }

    return render(request, 'details.html', context)


class EntriesListView(ListView):
    model = Entry
    paginate_by = 20
    context_object_name = 'entries'
    template_name = 'entries.html'
    ordering = ['-created_at']

