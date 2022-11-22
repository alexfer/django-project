from django.shortcuts import render
from modules.content.models import Entry
from django.views.generic.list import ListView


class HomeListView(ListView):
    template_name = 'home.html'
    queryset = Entry.objects.order_by('-created_at')[:10]


def AboutStaticView(request):
    file = open('modules/base/data/about.txt', 'r')
    if file.mode == 'r':
        description = file.read()
    else:
        description = 'About text'
    return render(request, 'about.html', {'description': description})
