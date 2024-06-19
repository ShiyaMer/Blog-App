from django.contrib import admin
from django.urls import path
#This file was made by me i copied code from webapp 's url.py
#import views here
from .import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


"""urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),# empty means i dont wont to when coming here g=from webapp 's urls include function cuts the path sepcified and what comes to blog's url id an empty string and views dot home is path
     path('post/<int:pk>/update',PostUpdateView.as_view(),
     name='post-update'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    #variable as primary key
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name='blog-about'),
     path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
]"""
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),#name as i may need to do a reverse lookup
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

