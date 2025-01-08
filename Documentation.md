# Steps
## Bot starts:
1. Check CSV/visited pages -> Save a local vers.

&nbsp;
&nbsp;
## Steps for robots_txt :robot:

1. Make sure base_url is valid.
  - Starts with _https://_ or _http://_.
  - Leads to an actual website.
  
2. Check if robots_txt exists, related to the base_url.
  - None: Return None, assuming full access to scrape website.
  - Found: Check if agent exists in robots_txt.
    - Found: Assume specific agent.
    - None: Assume agent '*'.
  - Find allowed/disallowed pages for specific agent.

&nbsp;
&nbsp;
## Steps for scraping. :knife:


### for url in urls:
2. Get HTML belonging to url.
3. Scrape HTML, saving _(unique/not in visited_pages list)_ found urls to a temp list.
4. Check found urls:
  - Do they (exactly) exist in disallowed?
    - No: Save url to a found_urls list, to check later.
    - Yes: Return False. _Do not scrape_.
  - Check allowed urls.
5. Redo 3 times _(for now)_.

&nbsp;
&nbsp;
## Steps for CSV. :file_folder:

1. Save all visited pages.
2. ???
3. Profit
