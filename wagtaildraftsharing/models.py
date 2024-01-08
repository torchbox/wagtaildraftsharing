import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.html import format_html


class WagtaildraftsharingLink(models.Model):
    key = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=False
    )
    revision = models.OneToOneField(
        "wagtailcore.Revision",
        on_delete=models.CASCADE,
        related_name="+",
    )
    is_active = models.BooleanField(default=True)
    active_until = models.DateTimeField(
        null=True, blank=True, help_text="Leave blank for no expiry"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        editable=False,
    )

    def __str__(self):
        return f"Revision {self.revision_id} of {self.revision.content_object}"

    class Meta:
        verbose_name = "Draftsharing Link"
        verbose_name_plural = "Draftsharing Links"

    @property
    def url(self):
        return reverse("wagtaildraftsharing:view", kwargs={"key": self.key})

    @property
    def share_url(self):
        return format_html(
            """<a data-wagtaildraftsharing-url
            class="button button-secondary button-small"
            target="_blank" rel="noopener noreferrer" href="{}">View</a>""",
            self.url,
        )
