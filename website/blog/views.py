from django.shortcuts import render
#utl necessary imports for previous projects
import urllib.request
import urllib.parse


posts = [
    {
        'author': 'Leonardo de Farias',
        'title': 'A Novel Approach of Deep Learning to Leukemia Detection',
        'link': urllib.request.urlopen(
            "https://github.com/Tofudog/C3BO-Cancer-Blood-Oncologist"
        )
    }
]

bibliography = [
    {
        'authors': 'abir et al.',
        'title': 'Explainable AI in Diagnosing and Anticipating Leukemia Using Transfer Learning Method',
        'journal': 'Computational Intelligence and Neuroscience',
        'annotation': 'This is my first annotation'
    }
]

#how we want to handle when user goes to this page
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    context = {'posts': posts}
    return render(request, 'blog/about.html', context)
    #return HttpResponse('<h1>Blog About</h1>')

def citations(request):
    context = {'bibliography': bibliography}
    return render(request, 'blog/citations.html', context)

