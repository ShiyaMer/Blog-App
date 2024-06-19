from django.contrib import admin

#Register models to show up on admin page
from .models import Post
admin.site.register(Post)
