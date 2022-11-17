from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from content.models import Entry
from django.contrib import messages
from comment.models import Comment
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _


# Create your views here.

def details(request, id):
    comments = Comment.objects.filter(entry_id=id, approved=True).order_by('-created_at')

    try:
        entry = Entry.objects.get(id=id)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    context = {
        'entry': entry,
        'title': entry.title,
        'comments': comments,
    }

    return render(request, 'details.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        content = request.POST['content']
        title = request.POST['title']
        if not title or not content:
            messages.error(request, _('All fields cannot be empty.'), extra_tags='alert alert-danger')
            return render(request, 'content/form.html', {
                'title': _('Create'),
            })
        else:
            entry = Entry(title=title, content=content)
            entry.user_id = request.user.id
            entry.save()
            return redirect('collection-entries')
    else:
        return render(request, 'content/form.html', {
            'title': _('Create'),
        })


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
def change(request, id):
    try:
        entry = Entry.objects.get(user_id=request.user.id, id=id)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    if request.method == 'POST':
        content = request.POST['content']
        title = request.POST['title']
        if not title or not content:
            messages.error(request, _('All fields cannot be empty.'), extra_tags='alert alert-danger')
            return render(request, 'content/form.html', {})
        else:
            entry.title = title
            entry.content = content
            entry.save()
            return redirect('collection-entries')
    else:
        return render(request, 'content/form.html', {
            'entry': entry,
            'title': _('Change'),
        })

@login_required
def destroy(request, id):
    try:
        entry = Entry.objects.get(user_id=request.user.id, id=id)
    except Entry.DoesNotExist:
        return render(request, 'errors/404.html', status=404)

    entry.delete()
    return redirect('collection-entries')
