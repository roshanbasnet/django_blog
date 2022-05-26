from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


class PostListView(ListView):
    model = Post
    # template urls for the class base view
    # <app>/<model>_<viewtype>.html but we can
    # also pass as below
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # ordering the post from newest to oldest by adding (-) on
    # on the ordering field
    ordering = ['-date_posted']


# To get single view
class PostDetailView(DetailView):
    model = Post


# To get single view
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
