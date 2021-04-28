from django.shortcuts import render

from . import util

#defines function 'index' that renders template encyclopedia/index.html 
#*requires arugment 'request' that for index will be blank
#*returns function 'render'
#*render takes request argument and renders the template argument
#*render provides the context argument {} to the template
#?{} is a dict of values, not sure how it is populated
#*dict key calls the value which is a function from encyclopedia/util.py

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entry(request):
    return render(request, "encyclopedia/wiki_entry.html", {
        
    })
    
def wiki_edit(request):
    return render(request, "encyclopedia/wiki_edit.html", {
        
    })
   
def wiki_new(request):
    return render(request, "encyclopedia/wiki_new.html", {
        
    })

def wiki_random(request):
    return render(request, "encyclopedia/wiki_random.html", {
        
    })
    