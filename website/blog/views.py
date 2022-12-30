from django.shortcuts import render
from django.http import HttpResponse

#selections on app content
home_info = {
    "author": "Leonardo de Farias",
    "title": "C-3BO",
    "Date_created": "10/5/2022"
}

class Citation:
    def __init__(self, title, authors, category, link, bias=None):
        self.title = title
        self.authors = authors
        self.category = category #domain of research
        self.link = link #create an acutal link out of string
        if (bias is not None):
            #have extra steps
            self.bias = bias #explanation on ambiguity
    def createLink(self):
        #set link to be an actual link
        return 0
    def __str__(self, style='MLA'):
        if (style=='MLA'):
            return f"{title}; {authors}; {category}; {link}"

#consider making each object in pastWork a Citation
pastWork = [
    t1 = "Using Convolutional Neural Networks (CNN) Image Recognition to "
    t1 += "Program the Artificially Learned C3BO: Cancer Blood Oncologist"
    t2 = "A Novel Approach of Deep Learning on Detection and Classification "
    t2 += "of Leukemic Cells and BCR-ABL1 Gene"
    {'title': t1, 'link': "None"}, 
    {'title': t2, 'link': "None"},
]

#of type Citation
citationList = [

]

def home(request):
    return render(request, 'blog/home.html', {'project': home_info})

def about(request):
    context = {"posts": pastWork}
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', context)

def citations(request):
    context = {}
    return render(request, 'blog/citations.html', context)
