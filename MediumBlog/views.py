from multiprocessing import context
from django.shortcuts import render, redirect
from blogs.models import Blogs, BlogCategories

# Create your views here.
def home(request):
    blogCategory = BlogCategories.objects.all().order_by('-published_on')
    blogs = Blogs.objects.all().order_by('-published_on')
    context = {
        'blogCategory' : blogCategory,
        'blogs' : blogs,
        'latestBlogs': blogs[:6],
        # 'count' : [1, 2, 3, 4, 5, 6],
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')