from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DetailView, UpdateView, DeleteView)
from .models import Post
# Create your views here.

class  PostListView(ListView):
    model = Post

class  PostCreateView(CreateView):
    model = Post
    fields = '_all_'
    success_url  = reverse_lazy("blog:all")

class  PostDetailView(DetailView):
    model = Post
    fields = "_all_"
    succes_url = reverse_lazy("blog:all")

class  PostUpdateView(UpdateView):
    model = Post
    fields = "_all_"
    succes_url = reverse_lazy("blog:all")

class  PostDeleteView(DeleteView):
    model = Post
    fields = "_all_"
    succes_url = reverse_lazy("blog:all")

