from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('category/<blogCategory>', views.category, name='blog-category'),
    path('<blogSlug>', views.readBlogs, name='read-blogs'),
]