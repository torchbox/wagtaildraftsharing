from wagtail.admin.panels import FieldPanel, ObjectList
from wagtail.snippets.views.snippets import SnippetViewSet

from wagtaildraftsharing.models import WagtaildraftsharingLink

from .settings import settings as draftsharing_settings


class WagtaildraftsharingLinkSnippetViewSet(SnippetViewSet):
    model = WagtaildraftsharingLink
    base_url_path = "wagtaildraftsharing"
    menu_icon = "view"
    menu_order = draftsharing_settings.ADMIN_MENU_POSITION
    add_to_settings_menu = False
    add_to_admin_menu = True
    list_display = ("__str__", "is_active", "created_by", "share_url")
    list_filter = ("is_active",)

    edit_handler = ObjectList([
        FieldPanel("revision", read_only=True),
        FieldPanel(
            "is_active",
            help_text=(
                "When false, the sharing link will not be viewable."
            )
        ),
        FieldPanel(
            "active_until",
            help_text=(
                "The link will not be viewable after this date. "
                "Leave blank if the link should never expire."
            )
        ),
    ])


    def get_queryset(self, request):
        return WagtaildraftsharingLink.objects.all().prefetch_related(
            "revision", "revision__content_object", "created_by"
        )
