from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from config.validations import validate_file_size, validate_file_type
from account.models import User, Ghost
# Create your models here.

class PostCategory(models.Model):
    class Meta:
        verbose_name = _("Post category")
        verbose_name_plural = _("Post categories")
    name = models.CharField(_("name"), max_length=250)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-created_at']
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name=_("category"))
    title = models.CharField(_("title"), max_length=250)
    image = models.ImageField(_("Image"), upload_to="blog/post/images", blank=True)
    content = RichTextUploadingField(_("content"), null=True)
    ghost_viewers = models.ManyToManyField(Ghost, verbose_name=_("ghost_viewers"), blank=True)
    user_viewers = models.ManyToManyField(User, verbose_name = _("user viewers"), blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30] + "..."
    
    def clean(self) -> None:
        if self.image:
            validate_file_type(self.image, ['.png', '.jpeg', '.jpg'])
            validate_file_size(self.image)
        return super().clean()

    def get_total_views(self)->int:
        g_views = self.ghost_viewers.count()
        u_views = self.user_viewers.count()
        return g_views + u_views