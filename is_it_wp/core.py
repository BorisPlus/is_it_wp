import requests


def is_it_have_wpadmin_page(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain.strip("/")}/wp-admin')
    return True if response.status_code == 200 else False


def is_it_have_readmehtml_page(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain.strip("/")}/readme.html')
    return True if response.status_code == 200 else False


def is_it_have_licensetxt_page(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain.strip("/")}/license.txt')
    return True if response.status_code == 200 else False


# Proudly powered by WordPress
# http://wordpress.org/
def is_it_have_wordpress_in_html(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain}')
    return True if b'wordpress' in response.content.lower() else False


def is_it_have_wp_content_in_html(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain}')
    return True if b'wp-content' in response.content.lower() else False


def is_it_have_wp_includes_in_html(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain}')
    return True if b'wp-includes' in response.content.lower() else False


def is_it_have_wp_any_in_html(domain, session=None):
    if session is None:
        session = requests.session()
    response = session.get(f'{domain}')
    return True if b'/wp-' in response.content.lower() else False


def check_content(domain, session=None):
    if session is None:
        session = requests.session()
    try:
        return dict(
            domain=domain,
            status='ok',
            check=dict(
                is_it_have_wordpress_in_html=is_it_have_wordpress_in_html(domain, session),
                is_it_have_wp_content_in_html=is_it_have_wp_content_in_html(domain, session),
                is_it_have_wp_includes_in_html=is_it_have_wp_includes_in_html(domain, session),
                is_it_have_wp_any_in_html=is_it_have_wp_any_in_html(domain, session)
            )
        )
    except:
        return dict(
            domain=domain,
            status='error',
            check=()
        )


def check(domain, session=None):
    if session is None:
        session = requests.session()
    try:
        return dict(
            domain=domain,
            status='ok',
            check=dict(
                is_it_have_wpadmin_page=is_it_have_wpadmin_page(domain, session),
                is_it_have_licensetxt_page=is_it_have_licensetxt_page(domain, session),
                is_it_have_readmehtml_page=is_it_have_readmehtml_page(domain, session),
                is_it_have_wordpress_in_html=is_it_have_wordpress_in_html(domain, session),
                is_it_have_wp_content_in_html=is_it_have_wp_content_in_html(domain, session),
                is_it_have_wp_includes_in_html=is_it_have_wp_includes_in_html(domain, session),
                is_it_have_wp_any_in_html=is_it_have_wp_any_in_html(domain, session)
            )
        )
    except:
        return dict(
            domain=domain,
            status='error',
            check=()
        )


if __name__ == "__main__":
    result = check('https://wpnice.ru')
    print(result)
