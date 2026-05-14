# Changelog

## [Unreleased]

### Added

- Support for Wagtail 7.0 LTS, 7.3, and 7.4 LTS.
- Support for Django 5.2 LTS and 6.0.
- Support for Python 3.13 and 3.14.

### Changed

- Bump minimum supported Python to 3.10.
- Bump minimum supported Wagtail to 7.0 (drops Wagtail 5.x and 6.x).
- Drop Wagtail 7.1 and 7.2 from the support matrix (both have reached end of life).

### Removed

- Removed Wagtail <6 compatibility branches in `wagtail_hooks.py` and `models.py`.
- Removed legacy vanilla-JS asset `wagtaildraftsharing/js/wagtaildraftsharing.js` (used only on Wagtail <6).
- Removed legacy `wagtailadmin/pages/revisions/_actions.html` template override (path no longer exists in Wagtail 7).

---

## [0.3.0] - 2025-05-21

### Changed

- Remove the ability to change which revision is shared on the draft sharing link edit page. (@mixxorz)

---

## [0.2.0] - 2025-03-28

### Added

- Support for **Wagtail 6**, including a Stimulus JS controller to replace legacy JS. (@stevejalim)
- New option to generate a **draft sharing link from the Action Menu** when a page has an unpublished draft. (@stevejalim)
- **Customizable verbose names** for draft sharing, implemented in a non-breaking way. (@stevejalim)
- **Customizable position** for the draft sharing menu item. (@stevejalim)
- **GitHub Actions CI** using `tox` and Python versions 3.9 to 3.12. (@stevejalim)
- Add fallback handling if the Clipboard API is not available. (@mixxorz)
- Add `X-Robots-Tag` header to prevent search engines from indexing draft sharing links. (@mixxorz)

### Changed

- **Menu icon** for draft sharing has been updated. (@stevejalim)
- Dropped Python 3.8 support (EOL). (@stevejalim)

---

## [0.0.4] - 2024-01-30

### Added

- Initial release. (@KIRA009)
