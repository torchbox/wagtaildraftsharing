document.addEventListener('DOMContentLoaded', () => {
    const getJSONConfig = (name) => {
        const config = document.querySelector(`script#${name}`);
        if (!config) {
            throw new Error('wagtail-config script not found');
        }
        return JSON.parse(config.textContent);
    }

    const createSharingLink = () => {
        const links = document.querySelectorAll('[data-wagtaildraftsharing-create]')

        const onClickLink = (e) => {
            e.preventDefault();
            const button = e.target;
            const revisionId = button.dataset.wagtaildraftsharingCreate;
            const originalButtonText = button.textContent;

            button.disabled = true;
            button.textContent = 'Copying...';

            const wagtailConfig = getJSONConfig('wagtail-config');
            const wagtaildraftsharingConfig = getJSONConfig('wagtaildraftsharing-config');

            fetch(wagtaildraftsharingConfig.urls.create, {
                method: 'POST',
                body: `revision=${revisionId}`,
                credentials: 'same-origin',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': wagtailConfig.CSRF_TOKEN,
                },
            }).then(async res => {
                if (res.ok) {
                    const data = await res.json();
                    const url = window.location.origin + data.url;
                    navigator.clipboard.writeText(url).then(() => {
                        button.textContent = 'Copied!';
                        setTimeout(() => {
                            button.textContent = originalButtonText;
                            button.disabled = false;
                        }, 3000);
                    })
                } else {
                    button.textContent = originalButtonText;
                    button.disabled = false;
                }
            }).finally(() => {
            });
        }

        links.forEach(link => {
            link.addEventListener('click', onClickLink);
        })
    };

    const copyLinksToClipboard = () => {
        const links = document.querySelectorAll('[data-wagtaildraftsharing-url]')

        const onClickLink = (e) => {
            e.preventDefault()
            const link = e.target;
            const url = link.href;

            navigator.clipboard.writeText(url).then(() => {
                // show success message
                link.textContent = 'Copied!'
                // hide message after 5 seconds
                setTimeout(() => {
                    link.textContent = 'Copy'
                }, 3000)
            })
        }

        links.forEach(link => {
            link.textContent = 'Copy';
            link.addEventListener('click', onClickLink);
        })
    };
    copyLinksToClipboard();
    createSharingLink();
});
