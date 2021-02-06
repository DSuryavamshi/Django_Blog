from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Dhanush',
        'title': 'Test',
        'content': 'Test blog 1',
        'date_posted': 'Feb 5, 2021 '
    },
    {
        'author': 'Sagar',
        'title': 'Test 2',
        'content': 'Test blog 2',
        'date_posted': 'Feb 5, 2021 '
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
