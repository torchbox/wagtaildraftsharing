from wagtail.snippets.views.snippets import SnippetViewSet

from wagtaildraftsharing.models import WagtaildraftsharingLink


class WagtaildraftsharingLinkSnippet(SnippetViewSet):
    model = WagtaildraftsharingLink
    base_url_path = "wagtaildraftsharing"
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    add_to_admin_menu = True
    list_display = ("__str__", "is_active", "created_by", "share_url")
    list_filter = ("is_active",)

    def get_queryset(self, request):
        return WagtaildraftsharingLink.objects.all().prefetch_related(
            "revision", "revision__content_object", "created_by"
        )
