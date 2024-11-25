import requests
from bs4 import BeautifulSoup

baseUrl = 'https://en.wikipedia.org'


my_agents = ['*', 'LavSpidey']


def setup_robot_txt():
    txt = get_robot_txt(baseUrl)
    parsed_text = read_robot_txt(txt)
    if parsed_text == "err":
        print("Error - Could not get robots txt.")
        exit(1)

    for agent in my_agents:
        allowed, disallowed = parsed_text[agent]
        print(f'Allowed: {allowed}, Disallowed: {disallowed}')


    # sort_allowed(parsed_text)


def get_robot_txt(base_url):
    result = requests.get(base_url + "/robots.txt")
    if result.status_code != 200:
        print(f"Error - Status code: {result.status_code}")
        exit(1)
    return result.text


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

# def sort_allowed(parsed_text):
#     robots_txt = set_agent(parsed_text, baseUrl)
#
#     allowed, disallowed = robots_txt[parsed_text]
#     return allowed, disallowed

# def set_agent(current_agent, base_url):
#     robot_txt = get_robot_txt(base_url)
#     agents = read_robot_txt(current_agent, robot_txt)
#     return agents

def crawl(agent):
    allowed, disallowed = sort_allowed(agent)
    print(f"Allowed: {allowed}, Disallowed: {disallowed}")
