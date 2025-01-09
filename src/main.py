import robotTxt
import scrape
import website
import csvHandling

if __name__ == '__main__':
    # Starting to scrape from Wikipedia.
    site = website.Website("https://wikipedia.org", None, None)
    domains = [site]

    # Check if CSV file exists - If not, creates it.
    csv_file = csvHandling.csv_start_up()
    csvHandling.add_to_csv(csv_file, domains)

    # csvHandling.print_csv_data()

    # Gets robot.txt file from base site.
    # for site in domains:
    #     robot_txt = robotTxt.setup_robot_txt(domains)

    # Returns base urls, allowed and disallowed pages to scrape.
    # scrape.scrape(domains, robot_txt[0], robot_txt[1])
