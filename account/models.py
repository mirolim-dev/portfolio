from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator

from config.validations import validate_file_size, validate_file_type
from .validations import validate_phone
from .utils import generate_username
# Create your models here.


class OwnerInfo(User):
    class Meta:
        verbose_name = _("Owner's Information")
        verbose_name_plural = _("Owner's Informations")
    major = models.CharField(_("major"), max_length=60, default="Software engineer")
    address = models.CharField(_("address"), max_length=100, null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=15)
    image = models.ImageField(_("image"), upload_to='owner/profile')
    cv = models.FileField(upload_to="owner/cv", null=True)
    bio = models.TextField(_("bio"), max_length=200)
    date_of_birth = models.DateField(_("Date of birth"), blank=True, null=True)
    is_visible = models.BooleanField(_("Visible"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)   
    updated_at = models.DateTimeField(_(""), auto_now=True)

    def __str__(self):
        return self.get_full_name()
    
    def save(self, *args, **kwargs) -> None:
        if not self.pk and OwnerInfo.objects.filter(is_active=True).exists():
            raise ValidationError(_("Before creating new owner you should change previouse user's is_visible field to False"))
        if not self.username:
            self.username = generate_username()
        return super().save(*args, **kwargs)

    def clean(self) -> None:
        # validate_phone(self.phone)
        validate_file_type(self.image, ['.png', '.jpeg', '.jpg'])
        validate_file_size(self.image)
        validate_file_type(self.cv)
        validate_file_size(self.cv)        
        return super().clean()

    def get_all_social_media(self):
        return self.socialmedia_set.select_related('owner')

    def get_the_age(self):
        from datetime import date, timedelta, datetime
        age = today.year - self.date_of_birth.year
        today = datetime.now().date()
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


class Contributer(User):
    class Meta:
        verbose_name = "Contributer"
        verbose_name_plural = "Contributers"
    phone = models.CharField(_("phone"), max_length=15, blank=True, null=True, unique=True)
    major = models.CharField(_("Major"), max_length=100)
    image = models.ImageField(_("Image"), upload_to="contributers/images")
    description = models.TextField(_("description"), max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contributer: {self.get_full_name()}"

    def clean(self) -> None:
        # validate_phone(self.phone)
        validate_file_type(self.image, ['.png', '.jpeg', '.jpg'])
        validate_file_size(self.image)     
        return super().clean()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        return super().save(*args, **kwargs)

    def get_all_social_media(self):
        return self.socialmedia_set.select_related('owner')


class SocialMedia(models.Model):
    class Meta:
        verbose_name = _("Social media")
        verbose_name_plural = _("Social medias")
        ordering = ["name"]
    name = models.CharField(_("name"), max_length=50)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, verbose_name=_("Social Media"), on_delete=models.CASCADE)
    link = models.URLField(_("Link"), max_length=200, unique=True)

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.social_media.name}"
    

class Ghost(models.Model):
    class Meta:
        verbose_name = _("Ghost")
        verbose_name_plural = _("Ghosts")
    ip_address = models.GenericIPAddressField(_("IP address"))

    def __str__(self):
        return f"Ghost: {self.id}"