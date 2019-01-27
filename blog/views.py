from django.shortcuts import render

# Create your views here.

from .models import Blog


def blog_page(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs': blogs})
