from django.contrib import admin
from .models import Post, Category, Tag, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'tag_list', 'title',
                    'description', 'image', 'create_date','update_date', 'like')
    
    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'short_content', 'create_date',
                    'update_date')


