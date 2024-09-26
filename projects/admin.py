from django.contrib import admin
from django.templatetags import static
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Category, Stack, Project, ProjectFeature
# Register your models here.

admin.site.register(Category)
admin.site.register(Stack)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'display_image', 
                    'created_at', 'updated_at',
                    'display_video_button', 'display_view_demo_button'
                    ]
    search_fields = ['name']
    list_filter = ['category']


    def display_image(self, obj):
        if obj.image:  # Assuming your model has an 'image' field
            url = obj.image.url
            format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', url, url)
        return None
    display_image.short_description = _("Image")

    def display_video_button(self, obj):
        if obj.video_url:  # Only display if a video URL is set
            return format_html(
                '<a href="{}" target="_blank"><button type="button">Play Video</button></a>', 
                obj.video_url
            )
        return "No video available"
    display_video_button.short_description = "Play Video"

    def display_view_demo_button(self, obj):
        if obj.production_url: #Only display if a Production(Demo) URL is set
            return format_html(
                '<a href="{}" target="_blank"><button type="button">View demo</button></a>', 
                obj.production_url
            )
        return "Demo doesn't exist"
    display_view_demo_button.short_description = "Production"

admin.site.register(Project, ProjectAdmin)


class ProjectFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name', 'display_image', 
                    'created_at', 'updated_at',
                    'display_video_button', 'display_view_demo_button'
                    ]
    search_fields = ['project__name', 'name']
    list_filter = ['project__category']


    def display_image(self, obj):
        if obj.image:  # Assuming your model has an 'image' field
            url = obj.image.url
            format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', url, url)
        return None
    display_image.short_description = _("Image")

    def display_video_button(self, obj):
        if obj.video_url:  # Only display if a video URL is set
            return format_html(
                '<a href="{}" target="_blank"><button type="button">Play Video</button></a>', 
                obj.video_url
            )
        return "No video available"
    display_video_button.short_description = "Play Video"

    def display_view_demo_button(self, obj):
        if obj.production_url: #Only display if a Production(Demo) URL is set
            return format_html(
                '<a href="{}" target="_blank"><button type="button">View demo</button></a>', 
                obj.production_url
            )
        return "Demo doesn't exist"
    display_view_demo_button.short_description = "Production"

admin.site.register(ProjectFeature, ProjectFeatureAdmin)
