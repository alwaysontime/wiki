from django.urls import path

from . import views

urlpatterns = [
    # the first argument (route) 
    # route is blank for the index route
    # the views.index argument calls the relevant function from encyclopedia\views.py
    # the name argument can be called in html - e.g. see the layout.html menu
    path("", views.index, name="index"),
    path("wiki_entry", views.wiki_entry, name="wiki_entry"),
    path("wiki_edit", views.wiki_edit, name="wiki_edit"),
    path("wiki_new", views.wiki_new, name="wiki_new"),
    path("wiki_random", views.wiki_random, name="wiki_random")
]
