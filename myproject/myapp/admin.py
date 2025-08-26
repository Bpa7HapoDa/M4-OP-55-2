from django.contrib import admin
from .models import Post, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','created_at')
    list_filter = ('category','tags')
    search_fields = ('title','content')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
