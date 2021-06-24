from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user','updated_at','image_1',)
    search_fields = ('title','user',)
