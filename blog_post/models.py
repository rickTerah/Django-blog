from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = settings.AUTH_USER_MODEL
class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # BlogPost.objects.filter()
        return self.filter(publish_date__lte=now)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    def published(self):
        now = timezone.now()
        # BlogPost.objects.filter()
        return self.get_queryset().published()

# Create your models here.
class BlogPost(models.Model): # blogpost_set -> queryset
    user = models.ForeignKey(User, default=1, null=True, on_delete = models.SET_NULL) # if we set on_delete = models.CASCADE then delete the user will cause deletion of all related stuffs
    title = models.CharField(max_length = 20, null=False)
    slug = models.SlugField()
    content = models.TextField(null = True, blank = True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    objects = BlogPostManager()

    class Meta:
        ordering = [ '-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"{self.id}/"
        # return reverse("blog_post:post_detail", kwargs = {{"id": self.id}})
    def get_edit_url(self):
        return f"edit/"

    def get_delete_url(self):
        return f"delete/"