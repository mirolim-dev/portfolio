from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

from config.validations import validate_file_size, validate_file_type
from account.models import OwnerInfo, Contributer
# Create your models here.
class Stack(models.Model):
    class Meta:
        verbose_name = _("Stack")
        verbose_name_plural = _("Stacks")
    name = models.CharField(_("name"), max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    name = models.CharField(_("name"), max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
    owner = models.ForeignKey(OwnerInfo, on_delete=models.CASCADE, verbose_name=_("owner"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"), blank=True, null=True)
    name = models.CharField(_("name"), max_length=150)
    image = models.ImageField(_("image"), upload_to=f"projects/images/{name}")
    video_url = models.URLField(_("video url"), max_length=200, null=True, blank=True)
    production_url = models.URLField(_("production url"), max_length=200, null=True, blank=True)
    stacks = models.ManyToManyField(Stack, verbose_name="stacks")
    contributers = models.ManyToManyField(Contributer, verbose_name=_("contributers"), blank=True, null=True)
    content = RichTextUploadingField(_("content"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return self.name[:20]
    
    def clean(self):
        validate_file_type(self.image, ['.jpg', '.png', '.jpeg'])
        validate_file_size(self.image)
        if not self.pk and self.owner:
            raise ValidationError(_("Owner Info should be created before projects have been created."))
        return super().clean()

class ProjectFeature(models.Model):
    class Meta:
        verbose_name = _("Project feature")
        verbose_name_plural = _("Project features")
        ordering = ['-created_at']
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_("project"))
    name = models.CharField(_("name"), max_length=100)
    image = models.ImageField(_("image"), upload_to=f"projects/images/{project.name}/features/{name}")
    video_link = models.URLField(_("video url"), max_length=200, blank=True, null=True)
    production_url = models.URLField(_("Production url"), max_length=200, blank=True, null=True)
    content = RichTextUploadingField(_("content"))

    created_at = models.DateField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self):
        return f"{self.project.name} | {self.name}"
    

    def clean(self) -> None:
        validate_file_size(self.image)
        validate_file_type(self.image, ['jpeg', 'jpg', 'png'])
        return super().clean()