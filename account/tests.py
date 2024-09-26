from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .models import OwnerInfo, SocialMedia
from .validations import validate_phone
from config.validations import validate_file_type, validate_file_size
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class OwnerInfoModelTest(TestCase):
    def setUp(self):
        # Create a sample image file
        self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

    def test_create_owner_info_valid(self):
        owner = OwnerInfo.objects.create(
            username="testuser",
            address="123 Test St",
            phone="+1234567890",
            image=self.image,
            bio="This is a bio",
            date_of_birth=date(1990, 1, 1)
        )
        self.assertTrue(OwnerInfo.objects.exists())
        self.assertEqual(owner.phone, "+1234567890")
        self.assertEqual(owner.address, "123 Test St")

    # def test_phone_validation(self):
    #     # Test valid phone numbers
    #     valid_phones = ["+1234567890", "+12345678901234", "1234567890"]
    #     for phone in valid_phones:
    #         try:
    #             validate_phone(phone)
    #         except ValidationError:
    #             self.fail(f"Phone number '{phone}' should be valid.")

    #     # Test invalid phone numbers
    #     invalid_phones = ["123", "abc1234567", "+12345", "+12345678901234567890"]
    #     for phone in invalid_phones:
    #         with self.assertRaises(ValidationError):
    #             validate_phone(phone)

    def test_file_validations(self):
        # Test valid image types
        valid_images = [
            SimpleUploadedFile("valid_image.png", b"file_content", content_type="image/png"),
            SimpleUploadedFile("valid_image.jpg", b"file_content", content_type="image/jpeg"),
        ]
        for image in valid_images:
            try:
                validate_file_type(image, ['.png', '.jpeg', '.jpg'])
                validate_file_size(image)
            except ValidationError:
                self.fail(f"Image '{image.name}' should be valid.")

        # Test invalid image type
        invalid_image = SimpleUploadedFile("invalid_image.gif", b"file_content", content_type="image/gif")
        with self.assertRaises(ValidationError):
            validate_file_type(invalid_image, ['.png', '.jpeg', '.jpg'])

        # Test invalid image size
        invalid_large_image = SimpleUploadedFile("large_image.jpg", b"x" * (3 * 1024 * 1024), content_type="image/jpeg")  # 3 MB
        with self.assertRaises(ValidationError):
            validate_file_size(invalid_large_image)

    def test_save_logic(self):
        OwnerInfo.objects.create(username="visible_user", is_visible=True)
        with self.assertRaises(ValidationError):
            OwnerInfo.objects.create(
                username="new_user",
                address="123 Test St",
                phone="+1234567890",
                image=self.image,
                bio="This is a bio",
                date_of_birth=date(1990, 1, 1)
            )

    def test_get_all_social_media(self):
        owner = OwnerInfo.objects.create(username="user", phone="+1234567890", image=self.image, bio="bio")
        social_media = SocialMedia.objects.create(owner=owner, name="Twitter", link="https://twitter.com/user")
        self.assertIn(social_media, owner.get_all_social_media())

#### **Tests for `SocialMedia` Model**

class SocialMediaModelTest(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.owner = OwnerInfo.objects.create(
            username="testowner",
            phone="+1234567890",
            image=self.image,
            bio="Bio text"
        )

    def test_create_social_media_valid(self):
        social_media = SocialMedia.objects.create(
            owner=self.owner,
            name="Facebook",
            link="https://facebook.com/user"
        )
        self.assertTrue(SocialMedia.objects.exists())
        self.assertEqual(social_media.name, "Facebook")
        self.assertEqual(social_media.link, "https://facebook.com/user")

    def test_social_media_string_representation(self):
        social_media = SocialMedia.objects.create(
            owner=self.owner,
            name="Instagram",
            link="https://instagram.com/user"
        )
        self.assertEqual(str(social_media), "Instagram")

    def test_social_media_verbose_name(self):
        social_media = SocialMedia.objects.create(
            owner=self.owner,
            name="LinkedIn",
            link="https://linkedin.com/user"
        )
        self.assertEqual(social_media._meta.verbose_name, _("Social media"))
        self.assertEqual(social_media._meta.verbose_name_plural, _("Social medias"))
