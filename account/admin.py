from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static
from .models import OwnerInfo, SocialLink, SocialMedia, Contributer
# Register your models here.

admin.site.register(SocialMedia)
class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

class OwnerInfoAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
    list_display = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'is_visible']
    list_filter = ['is_visible']
    exclude = ['is_active', 'is_superuser', 'is_staff', 'last_login', 'password', 'username', 'date_joined', 'groups', 'user_permissions']
admin.site.register(OwnerInfo, OwnerInfoAdmin)


class ContributerAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
    list_display = ['first_name', 'last_name', 'display_image', 'email', 'phone', 'major']
    exclude = ['is_active', 'is_superuser', 'is_staff', 'last_login', 'password', 'username', 'date_joined', 'groups', 'user_permissions']

    def display_image(self, obj):
        url = static("images/profile.jpg")
        if obj.image:  # Assuming your model has an 'image' field
            url = obj.image.url
        return format_html('<a href="{}"><img src="{}" width="50" height="50" /></a>', url, url)
    display_image.short_description = _("Image")
admin.site.register(Contributer, ContributerAdmin)