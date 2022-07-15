from multiprocessing import context
from operator import imod
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blogs, BlogCategories

# Create your views here.

def blogs(request):
    blogCategory = BlogCategories.objects.all()
    blogs = Blogs.objects.all().order_by('-published_on')
    context = {
        'blogCategory' : blogCategory,
        'blogData' : blogs,
    }
    return render(request, 'blog/blog.html', context)

def category(request, blogCategory):
    newCategory = BlogCategories.objects.get(category = blogCategory)
    relatedBlogs = Blogs.objects.all().order_by('-published_on')
    context = {
        'category' : newCategory,
        'relatedBlogs': relatedBlogs,
    }
    return render(request, 'blog/blog_category.html', context)

@login_required(login_url='/authentication/login/')
def readBlogs(request, blogSlug):
    newBlog = Blogs.objects.get(slug = blogSlug)
    relatedBlogs = Blogs.objects.all().order_by('-published_on')
    context = {
        'blog' : newBlog,
        'relatedBlogs': relatedBlogs,
    }
    return render(request, 'blog/read_blogs.html', context)
