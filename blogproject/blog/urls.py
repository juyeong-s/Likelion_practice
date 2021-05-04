from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name="post_list"),
    path('posts/<int:post_id>/', views.post_detail, name="post_detail"),
    path('posts/<int:post_id>/delete/', views.post_delete, name="post_delete"),
    path('posts/edit/<int:post_id>/', views.post_edit, name="post_edit"),
    path('posts/new/', views.post_new, name="post_new"),
]
