from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
    # list out objects , it could also be a search view
def blog_post_list_view(request):
    # for search you can say {qs = BlogPost.objects.filter(title_icontains= 'hello')}
    queryset = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        queryset = BlogPost.objects.filter(user=request.user)
    template_name = 'post_list.html'
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

def blog_post_detail_view(request, id):
    # obj = BlogPost.objects.get(id=id)
    obj = get_object_or_404(BlogPost, id = id)
    context = {
        "object": obj
    }
    return render(request, 'post_detail.html', context)

# @login_required(login_url = '/login')
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        obj = form.save() 
        alert = 'You have successfully added another blog.'
        obj.user = request.user
        # obj = BlogPost.objects.create(**form.cleaned_data) in Forms not ModelForm
        form = BlogPostForm()
    context = {
        "form": form
    }
    return render(request, 'post_create.html', context)
@staff_member_required
def blog_post_update_view(request, id):
    obj = get_object_or_404(BlogPost, id=id)
    form = BlogPostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form=BlogPostForm()
    context = {
        "form": form
    }
    return render(request, 'post_create.html', context)
@staff_member_required
def blog_post_delete_view(request, id):
    obj = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("/posts/")
    context = {
        "object": obj
    }
    return render(request, 'post_delete.html', context)
