from http import HTTPStatus
from requests.exceptions import HTTPError
import time
import requests

agent = 'LavSpidey'

def setup_robot_txt(base_urls):
    urls = {}
    for url in base_urls:
        txt = get_robot_txt(url)
        if not txt:
            print("Could not find a robots txt. Assuming full access to scrape.")
            return
        parsed_text = read_robot_txt(txt)
        if parsed_text == "err":
            print("Could not find a robots txt. Assuming full access to scrape.")
            return
        urls = sort_allowed(agent, parsed_text)

    return urls


def get_robot_txt(base_url):
    result = check_request(base_url)
    print(result)
    if not result:
        print("No robots txt.")
        return None
    return result.text


def check_request(base_url):
    retries = 3
    retry_codes = [
        HTTPStatus.TOO_MANY_REQUESTS,
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT,
    ]

    for r in range(retries):
        try:
            result = requests.get(base_url + "/robots.txt", headers= {
                'User-Agent': "LavSpidey"
            })
            result.raise_for_status()
            return result
        except HTTPError as http_err:
            code = http_err.response.status_code
            if code in retry_codes:
                time.sleep(r)
                continue
            return False


def read_robot_txt(robot_txt):
    current_agent = ''
    agents = {}
    for line in robot_txt.splitlines():
        # Skip empty lines and comments.
        if not line or line.isspace() or line.startswith("#"):
            continue

        parts = line.split(":", 1)
        name, value = parts[0].strip(), parts[1].strip()
        if name == "User-agent":
            current_agent = value
            continue

        allowed, disallowed = agents.get(current_agent, (set({}), set({})))
        if name == "Allow":
            allowed.add(value)
        elif name == "Disallow":
            disallowed.add(value)
        agents[current_agent] = (allowed, disallowed)
    return agents


def sort_allowed(specific_agent, parsed_text):
    allowed_set = set()
    disallowed_set = set()
    if specific_agent not in parsed_text.keys():
        print(f'\nAgent not found: {specific_agent}')
    else:
        allowed, disallowed = parsed_text[specific_agent]
        print(f'\nAgent found: {specific_agent}')
        allowed_set.update(allowed)
        disallowed_set.update(disallowed)
    return allowed_set, disallowed_set
