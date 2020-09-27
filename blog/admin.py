from django.contrib import admin
from django.db import models
from django.forms import Textarea
from blog.models import PostCategory, Post, Comment


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.HodelAdmin):
    list_display = (
        'title',
        'category',
        'published',
        'created_at',
        'comment_count'
    )

    list_filter = (
    'category__name',
    'published',
)

    autocomplete_fields = ['category']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 90})},
}

def comments_count(self, obj):


    return Comment.objects.filter(post=obj).count()
comments_count.short_description = 'Comments'

# python manage.py createsupperuser
# python manage.py runserver
