import json

import wagtail
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
    if int(wagtail.__version__[0]) < 6:
        SHARING_JS_TEMPLATE = """<script src="{}"></script>"""
        SHARING_JS_PATH = "wagtaildraftsharing/js/wagtaildraftsharing.js"
    else:
        SHARING_JS_TEMPLATE = """<script type="module" src="{}"></script>"""
        SHARING_JS_PATH = "wagtaildraftsharing/js/wagtaildraftsharing_controller.js"

    return format_html(
        SHARING_JS_TEMPLATE,
        static(SHARING_JS_PATH),
    ) + mark_safe(
        f"""
        <script id="wagtaildraftsharing-config" type="application/json">
            {json.dumps({
                'urls': {
                    'create': reverse('wagtaildraftsharing:create'),
                },
            })}
        </script>"""
    )
