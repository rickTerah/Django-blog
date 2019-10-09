from django.contrib import admin
from .models import BlogPost

# user display for models
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
    )
# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
