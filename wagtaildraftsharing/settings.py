from django.conf import settings

WAGTAILDRAFTSHARING_ADMIN_MENU_POSITION = getattr(
    settings,
    "WAGTAILDRAFTSHARING_ADMIN_MENU_POSITION",
    200,
)

WAGTAILDRAFTSHARING_VERBOSE_NAME = getattr(
    settings,
    "WAGTAILDRAFTSHARING_VERBOSE_NAME",
    "Draftsharing Link",
)

WAGTAILDRAFTSHARING_VERBOSE_NAME_PLURAL = getattr(
    settings,
    "WAGTAILDRAFTSHARING_VERBOSE_NAME_PLURAL",
    "Draftsharing Links",
)

WAGTAILDRAFTSHARING_MENU_ITEM_LABEL = getattr(
    settings,
    "WAGTAILDRAFTSHARING_MENU_ITEM_LABEL",
    "Create draft sharing link",
)

DEFAULT_MAX_AGE = 7 * 24 * 60 * 60  # 7 days
WAGTAILDRAFTSHARING_MAX_AGE = getattr(
    settings,
    "WAGTAILDRAFTSHARING_MAX_AGE",
    DEFAULT_MAX_AGE,
)
