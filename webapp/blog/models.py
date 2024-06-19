from django.db import models
#orm-object relation model database help
#diffrent database can be used
#database structures classes called models
from django.utils import timezone

from django.contrib.auth.models import User  
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    
    #auto_now:update the post to current date-time everytime the post was updated.#auto_now_add sets it to only the time it was created but cannot be updated
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):#so that i can have a little description when i print out object
        return self.title
    #reverse function instead of redirect
    #reverse returns the full url as a string since all posts are different
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
    