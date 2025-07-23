"""Utilities for generation app."""

# django-fernet-fields relies on the deprecated ``force_text`` helper which was
# removed in Django 5. To keep the dependency working we alias ``force_text`` to
# ``force_str`` here before any models import it.
from django.utils.encoding import force_str
import django.utils.encoding as encoding

if not hasattr(encoding, "force_text"):
    encoding.force_text = force_str  # type: ignore[attr-defined]

