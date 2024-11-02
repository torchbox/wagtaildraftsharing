import uuid

import wagtail
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from . import settings as draftsharing_settings


class WagtaildraftsharingLink(models.Model):
    key = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        primary_key=False,
    )
    revision = models.OneToOneField(
        "wagtailcore.Revision",
        on_delete=models.CASCADE,
        related_name="+",
    )
    is_active = models.BooleanField(default=True)
    active_until = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Leave blank for no expiry",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        editable=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the verbose names from settings,
        # in a way that doesn't trigger migrations
        self._meta.verbose_name = draftsharing_settings.WAGTAILDRAFTSHARING_VERBOSE_NAME
        self._meta.verbose_name_plural = (
            draftsharing_settings.WAGTAILDRAFTSHARING_VERBOSE_NAME_PLURAL
        )

    def __str__(self):
        return f"Revision {self.revision_id} of {self.revision.content_object}"

    class Meta:
        # These may be changed in __init__ from settings
        verbose_name = "Sharing Link"
        verbose_name_plural = "Sharing Links"

    @property
    def url(self):
        return reverse("wagtaildraftsharing:view", kwargs={"key": self.key})

    @property
    def share_url(self):
        # Make the existing link easily shareable.
        # Also note that the View button is changed into a "Copy" button via JS
        if int(wagtail.__version__[0]) < 6:
            template = """<a
                class="button button-secondary button-small"
                data-wagtaildraftsharing-url
                target="_blank"
                rel="noopener noreferrer"
                href="{}">View</a>"""
        else:
            template = """<a
                class="button button-secondary button-small"
                data-controller="wagtaildraftsharing"
                data-wagtaildraftsharing-snippet-url
                target="_blank"
                rel="noopener noreferrer"
                href="{}">View</a>"""

        return format_html(template, self.url)
