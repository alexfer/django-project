from django.shortcuts import render
from content.models import Entry
from django.views.generic.list import ListView


class HomeListView(ListView):
    model = Entry
    paginate_by = 10
    ordering = ['-created_at']
    template_name = 'home.html'


def AboutStaticView(request):
    file = open('base/data/about.txt', 'r')
    if file.mode == 'r':
        description = file.read()
    else:
        description = 'About text'
    return render(request, 'about.html', {'description': description})
