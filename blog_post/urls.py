from django.urls import path
from .views import (
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_create_view,
    blog_post_update_view,
    blog_post_delete_view
)

app_name = 'blog_post'
urlpatterns = [
    path('', blog_post_list_view, name = "post_list"),
    path('<int:id>/', blog_post_detail_view, name = "post_detail"),
    path('<int:id>/edit/', blog_post_update_view, name = "post_update"),
    path('<int:id>/delete/', blog_post_delete_view, name = "post_delete"),
]