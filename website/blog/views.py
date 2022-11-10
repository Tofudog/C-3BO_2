from django.shortcuts import render
from django.http import HttpResponse

#selections on app content
home_info = [{
    "author": "Leonardo de Farias",
    "project": "C-3BO",
    "Date created": "10/5/2022"
}]

def home(request):
    context = {"posts": home_info}
    return render(request, 'blog/home.html', context)

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

