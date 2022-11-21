from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from content.models import Entry
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
            return redirect('details', entry.id)
    else:
        form = CreateEntryForm()

    return render(request, 'content/entry-form.html', {
        'form': form,
        'title': _('Create Entry'),
    })


@login_required
def ChangeEntry(request, id):
    entry = Entry.objects.get(user_id=request.user.id, id=id)

    if request.method == 'POST':
        form = ChangeEntryForm(request.POST, instance=entry)
        if form.is_valid():
            messages.success(request, _('Entry successfully updated.'), extra_tags='alert alert-success')
            form.save(commit=True)
            return redirect('change-entry', entry.id)
    else:
        form = ChangeEntryForm(instance=entry)

    return render(request, 'content/entry-form.html', {
        'form': form,
        'entry': entry,
        'title': _('Change Entry'),
    })


def details(request, id):
    comments = Comment.objects.filter(entry_id=id, approved=True).order_by('-created_at')

    try:
        entry = Entry.objects.get(id=id)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    print(comments)

    context = {
        'entry': entry,
        'comments': comments,
    }

    return render(request, 'details.html', context)


@login_required
def collection(request):
    entries = Entry.objects.filter(user_id=request.user.id).order_by('-id')
    paginator = Paginator(entries, 20)
    page = request.GET.get('page')
    context = paginator.get_page(page)

    return render(request, 'content/collection.html', {
        'entries': context,
    })


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
