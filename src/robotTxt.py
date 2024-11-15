import requests
from bs4 import BeautifulSoup

baseUrl = 'https://en.wikipedia.org'


def crawl(agent):
    allowed, disallowed = sort_allowed(agent)
    print(f"Allowed: {allowed}, Disallowed: {disallowed}")


def sort_allowed(current_agent):
    robots_txt = set_agent(current_agent, baseUrl)
    if robots_txt == "err":
        print("Error - Could not get robots txt.")
        exit(1)

    allowed, disallowed = robots_txt[current_agent]
    return allowed, disallowed


def set_agent(current_agent, base_url):
    robot_txt = get_robot_txt(base_url)
    agents = read_robot_txt(current_agent, robot_txt)
    return agents


def get_robot_txt(base_url):
    result = requests.get(base_url + "/robots.txt")
    if result.status_code != 200:
        print(f"Error - Status code: {result.status_code}")
        exit(1)
    return str(result.text)


def read_robot_txt(current_agent, robot_txt):
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
