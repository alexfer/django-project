from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from content.models import Entry
from django.contrib import messages
from comment.models import Comment
from django.utils.translation import gettext_lazy as _


# Create your views here.

def show(request, id):
    comments = Comment.objects.filter(entry_id=id, approved=True).order_by('-created_at')

    try:
        entry = Entry.objects.get(id=id)
    except (Entry.DoesNotExist):
        return render(request, 'errors/404.html', status=404)

    context = {
        'entry': entry,
        'title': entry.title,
        'comments': comments,
    }

    return render(request, 'show.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        content = request.POST['content']
        title = request.POST['title']
        if not title or not content:
            messages.error(request, _('All fields cannot be empty.'), extra_tags='alert alert-danger')
            return render(request, 'content/create.html', {})
        else:
            entry = Entry(title=title, content=content)
            entry.user_id = request.user.id
            entry.save()
            return redirect('collection-entries')
    else:
        return render(request, 'content/create.html', {})


def collection(request):
    if not request.user.is_authenticated:
        return redirect('login')

    entries = Entry.objects.filter(user_id=request.user.id).order_by('-id')
    paginator = Paginator(entries, 20)
    page = request.GET.get('page')
    context = paginator.get_page(page)

    return render(request, 'content/collection.html', {
        'entries': context,
    })
