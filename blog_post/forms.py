from django import forms
from .models import BlogPost

# Create your forms here.
class BlogPostForm(forms.ModelForm):
    title = forms.CharField()
    slug = forms.SlugField()
    # email = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea())

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'slug',
            'publish_date'
        ]
    def cleaned_title(self):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title_iexact=title)
        # qs = BlogPost.objects.filter(title_iexact = title) or (title_icontain=title)
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        if qs.exists():
            raise forms.ValidationError('This is title has already been used. Please use another title.')
        else:
            return title