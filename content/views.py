from django.shortcuts import render
from content.models import Entry
from comment.models import Comment


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
