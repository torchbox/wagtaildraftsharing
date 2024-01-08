import json

from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from wagtail_factories import PageFactory

from wagtaildraftsharing.models import WagtaildraftsharingLink
from wagtaildraftsharing.views import CreateSharingLinkView, SharingLinkView


User = get_user_model()


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.superuser = User.objects.create_superuser(
            username="test", password="test"
        )
        cls.factory = RequestFactory()

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

    def test_create_sharing_link_view(self):
        revision = self.create_revision()
        request = self.factory.post(
            "/create/",
            {
                "revision": revision.id,
            },
        )
        request.user = self.superuser

        response = CreateSharingLinkView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(
            response_data["url"], WagtaildraftsharingLink.objects.get().url
        )

    def test_sharing_link_view(self):
        revision = self.create_revision()
        sharing_link = WagtaildraftsharingLink.objects.create(
            revision=revision, created_by=self.superuser
        )

        request = self.factory.get(f"/{sharing_link.key}/")
        response = SharingLinkView.as_view()(request, key=sharing_link.key)

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, f"<title>{revision.as_object().title}</title>"
        )
