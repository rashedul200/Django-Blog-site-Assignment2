from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.





class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=150)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Blog(models.Model):
    status = [
        (0, 'Draft'),
        (1, 'Publish')
    ]
    title = models.CharField(max_length=200, help_text= "Enter Your Post Title Here.")
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=150)
    featured = models.ImageField(upload_to= 'featured_image/', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    post_status = models.IntegerField(choices=status, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length= 200, blank=True, null= True)
    meta_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
