from django.forms import ModelForm

from wagtaildraftsharing.models import WagtaildraftsharingLink


class CreateWagtaildraftsharingLinkForm(ModelForm):
    class Meta:
        model = WagtaildraftsharingLink
        fields = ["revision"]

    def clean(self):
        # Since we are using get_or_create, we don't need to check for uniqueness
        return
