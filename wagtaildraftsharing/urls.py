from django.urls import path

from wagtaildraftsharing.views import CreateSharingLinkView, SharingLinkView


urlpatterns = [
    path("<uuid:key>/", SharingLinkView.as_view(), name="view"),
    path("create/", CreateSharingLinkView.as_view(), name="create"),
]

app_name = "wagtaildraftsharing"
