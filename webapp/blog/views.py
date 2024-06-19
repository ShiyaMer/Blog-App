from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from typing import Any
from django.db.models.query import QuerySet

from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #for classes
from django.contrib.auth.models import User

#this was the first place i made change as in imported the httpResponse
#then i create a url file in blog directory
#posts=[#earlier i was passing this dummy data.Now i use the database data

def home(request):
    """return HttpResponse('<h1>Blog Home</h1>')"""
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
def about(request):
    #return HttpResponse('<h1>About Page</h1>')
    return render(request,'blog/about.html',{'title':"TitlePassed"})

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'#as in reallife it looks for object.list
    #<app>/<model>_<viewtype>.html conevection to be followed
    ordering=['-date_posted']
    paginate_by=5 #for diffrent pages
    #class saves code no need of render

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model=Post

class PostDeleteView(LoginRequiredMixin ,DeleteView):
    model=Post
    success_url='/'  



class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'#as in reallife it looks for object.list
    #<app>/<model>_<viewtype>.html conevection to be followed
    paginate_by=5 #for diffrent pages
    #class saves code no need of render  
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

         