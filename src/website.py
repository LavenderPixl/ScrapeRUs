from urllib.parse import urlparse

class Website:
    def __init__(self, url, allowed, disallowed):
        self.url = url
        self.domain = urlparse(url).netloc
        self.allowed = allowed
        self.disallowed = disallowed
        # self.robots_txt = robots_txt