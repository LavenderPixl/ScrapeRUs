import requests
from bs4 import BeautifulSoup

gathered_links = set()


# Gets site and returns HTML.
def get_html(url):
    page = requests.get(url)
    if page.status_code != 200:
        print(f"Error - Status code: {page.status_code}")
        exit(1)
    return BeautifulSoup(page.content, 'html.parser')


# def check_if_allowed(url):

# Need to find all Links on site, then check if they're in Disallowed.
# if so - Don't scrape. If not, scrape following site (IF IT CONTAINS SAME MAIN URL)
# Allowed sites (Dataset = Key: BaseUrls | Value: Specific)



# Scrapes site for URLs
def scrape_for_urls(html):
    for link in html.find_all('a'):
        gathered_links.add(link.get('href'))
    print(gathered_links)


def scrape(urls):
    for url in urls:
        html = get_html(url)

        if check_if_allowed(url):
            scrape_for_urls(html)
