from django.shortcuts import render, redirect
from content.models import Entry
from comment.models import Comment


# Create your views here.

def comment(request, id):
    try:
        entry = Entry.objects.get(id=id)
    except (Entry.DoesNotExist):
        return render(request, 'errors/404.html', status=404)
