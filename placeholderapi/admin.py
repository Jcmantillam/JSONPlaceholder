from django.contrib import admin
from .models import BlogUser, Post, Comment

# Register your models here.
admin.site.register(BlogUser)
admin.site.register(Post)
admin.site.register(Comment)