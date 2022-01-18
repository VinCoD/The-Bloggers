from django.contrib import admin
from .models import Headline, Post
# Register your models here.

admin.site.site_header = "The Bloggers Admin"
admin.site.site_title = "The Bloggers Admin"
admin.site.register(Headline)
admin.site.register(Post)