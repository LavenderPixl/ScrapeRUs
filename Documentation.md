# Steps / Thought process.

## Bot starts:

1. CSV

- Check if CSV file exists / Run startup script.
  - Found: Continue to next step.
  - Not found: Create a new CSV file, and continue.

  &nbsp;
- Check CSV for non-scraped sites
  - None found: Instantiate website (ex: Wikipedia), as start point.
  - List not empty & includes a site with 'Visited' field set to False: Continue scraping those sites. 


## Steps for robots_txt :robot:

1. Make sure base_url/domain is valid.
   - Starts with _https://_ or _http://_.
   - Leads to an actual website.

   &nbsp;
2. Check if robots_txt exists, related to the domain.
   - None: Return None, assuming full access to scrape website.
   - Found: Check if agent exists in robots_txt.
       - Found: Assume specific agent.
       - None: Assume agent '*'.
   - Find allowed/disallowed pages for specific agent.

&nbsp;

## Steps for scraping. :knife:

### for url in urls:

1. Get HTML belonging to url.
2. Scrape HTML, saving _(unique/not in visited_pages list)_ found urls to a temp list.
3. Check temp list:
- Do they (exactly) exist in disallowed?
    - No: Save url to a found_urls list, to check later.
    - Yes: Return False. _Do not scrape_.
- Check allowed urls.

4. Redo 3 times _(for now)_.

&nbsp;
&nbsp;

## Steps for CSV. :file_folder:

1. Save all visited pages in CSV file.
2. ???
3. Profit
