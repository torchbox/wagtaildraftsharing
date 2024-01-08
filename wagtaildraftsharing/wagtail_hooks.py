import json

from django.templatetags.static import static
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from wagtail import hooks
from wagtail.snippets.models import register_snippet

from wagtaildraftsharing.actions import (
    register_wagtaildraftsharing_log_actions,
)
from wagtaildraftsharing.snippets import WagtaildraftsharingLinkSnippet


register_snippet(WagtaildraftsharingLinkSnippet)

hooks.register("register_log_actions")(
    register_wagtaildraftsharing_log_actions
)


@hooks.register("insert_global_admin_js")
def editor_js():
    return (
        format_html(
            """
        <script src="{}"></script>
        """,
            static("wagtaildraftsharing/js/wagtaildraftsharing.js"),
        )
        + mark_safe(
            f"""
        <script id="wagtaildraftsharing-config" type="application/json">
            {json.dumps({
                'urls': {
                    'create': reverse('wagtaildraftsharing:create'),
                },
            })}
        </script>"""
        )
    )
