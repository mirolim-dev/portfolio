import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_file_type(file, required_types=['.pdf', '.docx', '.doc']):
    """
    Validate that the file's extension matches one of the allowed types.
    The error message is dynamic and translatable.
    
    :param file: The file being uploaded.
    :param required_types: A list of allowed file extensions.
    :raises ValidationError: If the file extension is not in the allowed types.
    """
    ext = os.path.splitext(file.name)[1].lower()  # Get the file extension
    if ext not in required_types:
        # Use gettext to mark the error message for translation
        allowed_types = ', '.join(required_types)
        raise ValidationError(
            _("Unsupported file type. Allowed types are: %(allowed_types)s.") % {'allowed_types': allowed_types}
        )


def validate_file_size(file, required_size=2):
    """
    Validate that the file size does not exceed the required size.
    The error message is dynamic and translatable.
    
    :param file: The file being uploaded.
    :param required_size: The maximum allowed file size in megabytes.
    :raises ValidationError: If the file size exceeds the limit.
    """
    file_size = file.size
    max_size = required_size * 1024 * 1024  # Convert MB to bytes
    
    if file_size > max_size:
        raise ValidationError(
            _("File size exceeds %(required_size)d MB limit.") % {'required_size': required_size}
        )