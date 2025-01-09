import requests
from bs4 import BeautifulSoup

visited_links = set()
gathered_links = set()


def scrape(urls, allowed, disallowed):
    """
    :param urls: Base urls.
    :param allowed:
    :param disallowed:
    :return:
    """
    for url in urls:
        check_url(url)

    # for url in urls:
    #     html = get_html(url)
    #     gathered_links.add(scrape_for_urls(html))
    #
    #     check_url(url, allowed, disallowed)

def get_html(url):
    """
    Gets HTML page from the given URL.
    :param url: Full url, to scrape
    :return: BeautifulSoup object
    """
    page = requests.get(url)
    if page.status_code != 200:
        print(f"Error - Status code: {page.status_code}")
        exit(1)
    return BeautifulSoup(page.content, 'html.parser')


def scrape_for_urls(html):
    """
    Scrapes given HTML for URLS and returns a set of URLS.
    :param html:
    :return: Links gathered from HTML page.
    """
    for link in html.find_all('a'):
        if link.get('href') not in gathered_links:
            gathered_links.add(link.get('href'))

    return gathered_links


def check_url(base_url, allowed, disallowed):
    """
    Checks given URL against given allowed/disallowed URLs.
    :param base_url: ex: https://www.google.com
    :param allowed: ex: /w/api.php?action=mobileview&
    :param disallowed: /w/
    :return: True/False
    """
    for i in disallowed:
        if base_url == i:
            return False

    for i in allowed:
        if base_url == i:
            return True

    return True


# Need to find all Links on site, then check if they're in Disallowed.
# if so - Don't scrape. If not, scrape following site
# Allowed sites (Dataset = Key: BaseUrls | Value: Specific)
