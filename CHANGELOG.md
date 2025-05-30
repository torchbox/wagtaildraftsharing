# Changelog

## [Unreleased]

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
