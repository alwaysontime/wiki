from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    # the first argument is the URL route the browser requests
    # route is blank for the index route
    # the views.FUNCTION argument calls the relevant function from views.py
    # the name argument can be called - e.g. in layout.html
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("wiki_edit", views.wiki_edit, name="wiki_edit"),
    path("wiki_new", views.wiki_new, name="wiki_new"),
    path("wiki_random", views.wiki_random, name="wiki_random"),
    path("search", views.search, name="search"),
    path("wiki_save", views.wiki_save, name="wiki_save"),
]
