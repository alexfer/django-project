from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

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

    sendmail.send(
       request.POST.get('email'),
       'Mew Comment',
       'Posted new comment to {}'.format(url),
    )

    comment = Comment(author=request.POST['author'], comment=request.POST['message'], approved=True)
    comment.entry = entry
    comment.save()

    return HttpResponseRedirect(url)
