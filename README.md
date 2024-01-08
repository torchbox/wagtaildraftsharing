wagtaildraftsharing
===============

Share [Wagtail](https://wagtail.io) drafts with private URLs.

``wagtaildraftsharing`` makes it easier to share Wagtail draft content for review by users who don't have access to the Wagtail admin site. It allows you to generate random urls to expose the revisions of your Wagtail pages.

## Setup
Install the package using pip:

```bash
pip install wagtaildraftsharing
```

Add ``wagtaildraftsharing`` as an installed app in your Django settings:

```python
# in settings.py
INSTALLED_APPS = (
    ...
    'wagtaildraftsharing',
    'wagtail.admin',
    ...
)
```
Since ``wagtaildraftsharing`` overrides one of the ``wagtail.admin`` templates, it must be listed before ``wagtail.admin`` in the ``INSTALLED_APPS`` list.

This package also makes use of ``wagtail.snippets``, so it must be included in your list of installed apps.

Run migrations to create the required database tables:

```bash
python manage.py migrate wagtaildraftsharing
```

Add the ``wagtaildraftsharing`` urls to your ``urls.py``:

```python
# in urls.py
import wagtaildraftsharing.urls as wagtaildraftsharing_urls

urlpatterns += [
    path("wagtaildraftsharing/", include(wagtaildraftsharing_urls)), # or whatever url you want
]
```

Each draft in the history page for any page (/admin/pages/\<id\>/history/) will now have an additional action - ``Copy external sharing url``. Clicking this will generate a random url (and copy it to the clipboard) that can be shared with anyone. The url will display the draft version of the page.

![Screenshot](https://raw.githubusercontent.com/KIRA009/wagtaildraftsharing/main/docs/images/history.png)

All generated links can be viewed at ``/admin/wagtaildraftsharing/``.

![Screenshot](https://raw.githubusercontent.com/KIRA009/wagtaildraftsharing/main/docs/images/sharinglinks.png)

Each link can be edited to expire at a certain date, or to be disabled immediately.

![Screenshot](https://raw.githubusercontent.com/KIRA009/wagtaildraftsharing/main/docs/images/sharinglink.png)

## Settings
The following settings can be added to your Django settings file:

### ``WAGTAILDRAFTSHARING_MAX_AGE``
The default expiry time for generated links, in seconds. Defaults to 1 week. Set it to a negative value to disable expiry.
