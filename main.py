import requests
from bs4 import BeautifulSoup

baseUrl = 'https://en.wikipedia.org'


def setup_robot_txt(baseurl):
    result = requests.get(baseurl + "/robots.txt")
    if result.status_code != 200:
        return "err"

    agents = {}
    current_agent = "*"
    for line in result.text.splitlines():
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


def sort_allowed():
    robotstxt = setup_robot_txt(baseUrl)
    if robotstxt == "err":
        print("error!")
        exit(1)

    allowed, disallowed = robotstxt["IsraBot"]
    print(f"Agent: '*' \n Allow: {allowed} \n Disallow: {disallowed}")


if __name__ == '__main__':
    sort_allowed()
    # robotstxt = setup_robot_txt(baseUrl)

    # for agent in robotstxt:
    #     allowed, disallowed = robotstxt[agent]
    #     print(f"{agent}: allow={allowed}, disallow={disallowed}")
