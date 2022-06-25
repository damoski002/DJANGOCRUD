from pyexpat import model
from attr import fields
from django.views.generic.edit import (Createview, DetailView, UpdateView, DeleteView)
from .models import Post

class blogAppCreateView(Createview):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class blogAppDetailsview(DetailView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class blogAppUpdateview(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class blogAppDeleteview(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

