from textwrap import dedent
from unittest.mock import patch

import wagtail
from django.test import TestCase
from wagtail_factories import PageFactory

from ..models import WagtaildraftsharingLink


class TestWagtaildraftsharingLinkModel(TestCase):
    def create_revision(self):
        page = PageFactory()

        # create the first revision
        page.save_revision().publish()

        old_title = page.title
        new_title = f"New {old_title}"
        page.title = new_title

        # create the second revision with a new title
        page.save_revision().publish()

        page.refresh_from_db()
        earliest_revision = page.revisions.earliest("created_at")
        return earliest_revision

    def test_str_method(self):
        # Just chasing 100% coverage
        revision = self.create_revision()
        link = WagtaildraftsharingLink.objects.create(
            revision=revision,
        )
        self.assertEqual(str(link), f"Revision {revision.id} of New Test page")

    def test_url_method(self):
        link = WagtaildraftsharingLink.objects.create(
            revision=self.create_revision(),
        )
        expected_url = f"/wagtaildraftsharing/{link.key}/"
        self.assertEqual(link.url, expected_url)

    @patch.object(wagtail, "__version__", "5.0.0")  # only first digit matters
    def test_share_url_method__wagtail_5(self):
        link = WagtaildraftsharingLink.objects.create(
            revision=self.create_revision(),
        )
        expected = dedent(
            f"""<a
                class="button button-secondary button-small"
                data-wagtaildraftsharing-url
                target="_blank"
                rel="noopener noreferrer"
                href="/wagtaildraftsharing/{link.key}/">View</a>"""
        )
        self.assertEqual(dedent(link.share_url), expected)

    @patch.object(wagtail, "__version__", "6.0.0")  # only first digit matters
    def test_share_url_method__wagtail_6(self):
        link = WagtaildraftsharingLink.objects.create(
            revision=self.create_revision(),
        )
        expected = dedent(
            f"""<a
                class="button button-secondary button-small"
                data-controller="wagtaildraftsharing"
                data-wagtaildraftsharing-snippet-url
                target="_blank"
                rel="noopener noreferrer"
                href="/wagtaildraftsharing/{link.key}/">View</a>"""
        )
        self.assertEqual(dedent(link.share_url), expected)
