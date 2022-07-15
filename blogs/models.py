from email.policy import default
from pyexpat import model
from unicodedata import category
from django.db import models
from autoslug import AutoSlugField
from django.forms import ImageField
from tinymce.models import HTMLField


categoryChoices = (
    ("physics", "physics"),
    ("ai", "ai"),
    ("ml", "ml"),
    ("technology", "technology"),
    ("mathematics", "mathematics"),
    ("python", "python"),
    ("universe", "universe"),
    ("sports", "sports"),
    ("music", "music"),
    ("entertainment", "entertainment"),
)

# Create your models here.
class Blogs(models.Model):
    author = models.CharField(max_length=255, default='Atanu')
    authorImg = models.FileField(upload_to="author/", max_length=500, default="author/admin.jpg")
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length= 255,
        choices=categoryChoices,
        default='physics',
    )
    body = HTMLField(default=None)
    tags = models.CharField(max_length=355, default=None, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, max_length=255, default=None)
    img1 = models.FileField(upload_to="blog_images/", max_length=500, default=None)
    img2 = models.FileField(upload_to="blog_images/", max_length=500, default=None, null=True, blank=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogCategories(models.Model):
    category = models.CharField(max_length=355)
    description = models.CharField(max_length=255)
    categoryImg = models.FileField(upload_to="category_images/", max_length=500, default=None)
    published_on = models.DateTimeField(auto_now_add=True)