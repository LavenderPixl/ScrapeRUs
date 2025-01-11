from numpy.matlib import empty

import robotTxt
import scrape
import website
import csvHandling

if __name__ == '__main__':
    # Check if CSV file exists | True: Save local vers. | False: Create it.
    csv_file = csvHandling.csv_start_up()

    # Check CSV for visited pages and if there are any with field 'scraped' as False.
    not_scraped = csvHandling.check_if_scraped(csv_file)

    if not_scraped is None or not not_scraped:
        # Starting to scrape from Wikipedia.
        site = website.Website("https://wikipedia.org", None, None, False)
        domains = [site]
        print('All scraped.')
    else:
        domains = not_scraped
        print('Not scraped:', not_scraped)

    # Gets robot.txt file from base site.
    for site in domains:
        robot_txt = robotTxt.setup_robot_txt(domains)
    #
    # csvHandling.add_to_csv(csv_file, domains)
    # csvHandling.print_csv_data(csv_file)

    # Returns base urls, allowed and disallowed pages to scrape.
    # scrape.scrape(domains, robot_txt[0], robot_txt[1])
