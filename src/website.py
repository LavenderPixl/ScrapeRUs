from urllib.parse import urlparse

class Website:
    def __init__(self, url, allowed, disallowed, scraped):
        self.url = url
        self.domain = urlparse(url).netloc
        self.allowed = allowed
        self.disallowed = disallowed
        self.visited = scraped
        # self.robots_txt = robots_txt