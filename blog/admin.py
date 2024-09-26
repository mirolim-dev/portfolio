from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import PostCategory, Post
# Register your models here.

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', "display_total_posts"]
    def display_total_posts(self, obj):
        return obj.post.objects_set.count()
    display_total_posts.short_descriptiom = _("Total posts")
admin.site.register(PostCategory, PostCategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', "display_title", 'display_total_views', 'created_at', 'updated_at']
    exclude = ['ghost_viewers', 'user_viewers']
    readonly_fields = ['display_total_views']

    list_filter = ['category']

    def display_title(self, obj):
        return obj.title[:15] + '...'
    display_title.short_description = _("title")

    def display_total_views(self, obj):
        return obj.get_total_views()
    display_total_views.short_description = _("total views")
admin.site.register(Post, PostAdmin)