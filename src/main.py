from numpy.matlib import empty

import robotTxt
import scrape
import website
import csvHandling
from src.csvHandling import check_if_exists

if __name__ == '__main__':
    # Check if CSV file exists | True: Save local vers. | False: Create it.
    # TODO: Check csv_list instead of file, for better optimization.
    csv_file = csvHandling.csv_start_up()

    # Check CSV for visited pages and if there are any with field 'scraped' as False.
    is_scraped = csvHandling.check_if_scraped(csv_file)

    if is_scraped is None or not is_scraped:
        # No links that need scraping.
        site = website.Website("https://wikipedia.org", None, None, False)
        is_new = check_if_exists(csv_file, site)
        if is_new:
            domains = [site]

        # TODO: Check if we've visited the site before - Is allowed/disallowed filled?
        # Starting to scrape from Wikipedia.

        print('All scraped.')
    else:
        # Links that need scraping...
        domains = is_scraped
        print('Not scraped:', is_scraped)

    # Gets robot.txt file from base site.
    for site in domains:
        robot_txt = robotTxt.setup_robot_txt(domains)
    #
    # csvHandling.add_to_csv(csv_file, domains)
    # csvHandling.print_csv_data(csv_file)

    # Returns base urls, allowed and disallowed pages to scrape.
    # scrape.scrape(domains, robot_txt[0], robot_txt[1])
