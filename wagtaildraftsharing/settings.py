from django.conf import settings

WAGTAIL_DRAFTSHARING_ADMIN_MENU_POSITION = getattr(
    settings, "WAGTAIL_DRAFTSHARING_ADMIN_MENU_POSITION", 200
)
