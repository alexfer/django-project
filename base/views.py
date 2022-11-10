from django.shortcuts import render
from content.models import Entry


# Create your views here.

def index(request):
    context = {
        'entries': Entry.objects.all().order_by('-id')[:10:1],
        'title': 'Latest News',
    }

    return render(request, 'index.html', context)


def about(request):
    file = open('base/data/about.txt', 'r')
    if file.mode == 'r':
        description = file.read()
    else:
        description = 'About text'
    return render(request, 'about.html', {'title': 'About', 'description': description})

