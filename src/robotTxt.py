import requests

baseUrl = 'https://en.wikipedia.org'
my_agents = ['*', 'LavSpidey']


def setup_robot_txt():
    txt = get_robot_txt(baseUrl)
    parsed_text = read_robot_txt(txt)
    if parsed_text == "err":
        print("Error - Could not get robots txt.")
        exit(1)

    for agent in my_agents:
        if agent in parsed_text:
            allowed, disallowed = parsed_text[agent]
            print(f'\nAgent in: {agent}')
            print(f'Allowed: {allowed}, Disallowed: {disallowed}')
        else:
            print(f'\nAgent not in robots txt. : {agent}')


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
