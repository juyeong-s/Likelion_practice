from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('sns/', views.sns, name='sns'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post_delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post_edit/<int:post_id>/', views.post_edit, name='post_edit'),
    # path('<int:post_id>/comment_new/', views.comment_new, name='comment_new'),
]