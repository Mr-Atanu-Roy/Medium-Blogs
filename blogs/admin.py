from django.contrib import admin
from blogs.models import Blogs, BlogCategories

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'img1', 'img2', 'likes', 'comments', 'published_on')

class BlogCategoriesAdmin(admin.ModelAdmin):
    list_display = ('category', 'description', 'categoryImg')

admin.site.register(Blogs, BlogAdmin)
admin.site.register(BlogCategories, BlogCategoriesAdmin)