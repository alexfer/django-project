from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from comment.forms import CommentForm
from content.models import Entry
from django.views.generic.list import ListView
from django.contrib import messages
from comment.models import Comment
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from .forms import CreateEntryForm, ChangeEntryForm


@login_required
def CreateEntry(request):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('details', entry.slug)
    else:
        form = CreateEntryForm()

    return render(request, 'content/entry-form.html', {
        'form': form,
        'title': _('Create Entry'),
    })


@login_required
def ChangeEntry(request, slug):
    entry = Entry.objects.get(user_id=request.user.id, slug=slug)

    if request.method == 'POST':
        form = ChangeEntryForm(request.POST, instance=entry)
        if form.is_valid():
            messages.success(request, _('Entry successfully updated.'), extra_tags='alert alert-success')
            form.save(commit=True)
            return redirect('change-entry', entry.slug)
    else:
        form = ChangeEntryForm(instance=entry)

    return render(request, 'content/entry-form.html', {
        'form': form,
        'entry': entry,
        'title': _('Change Entry'),
    })


def details(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    comments = Comment.objects.filter(entry_id=entry.id, approved=True).order_by('-created_at')

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
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


class EntryListView(LoginRequiredMixin, ListView):
    paginate_by = 20
    context_object_name = 'entries'
    template_name = 'content/collection.html'

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).order_by('-id')


@login_required
def DestroyEntry(request, id):
    try:
        entry = Entry.objects.get(user_id=request.user.id, id=id)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    if request.method == 'POST':
        entry.delete()
        return redirect('collection-entries')

    return render(request, 'content/delete-entry.html', {
        'entry': entry,
    })
