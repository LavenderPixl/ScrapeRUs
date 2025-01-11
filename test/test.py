import unittest

from src import website
from src.csvHandling import *
from src.robotTxt import *
from src.scrape import *
from bs4 import BeautifulSoup


def test_get_robots_txt():
    conn = open("testRobotTxt.txt", "r")
    robots_txt = conn.read()
    conn.close()
    result = read_robot_txt(robots_txt)
    return result


class TestRobotTxt(unittest.TestCase):
    # Retrieving LOCAL robot.txt file.
    def test_read_robot_txt(self):
        actual = test_get_robots_txt()
        expected = {'k2spider': (set(), {'/'}), 'NPBot': (set(), {'/'}), '*': (
            {'/api/rest_v1/?doc', '/w/load.php?', '/w/api.php?action=mobileview&'},
            {'/api/', '/w/', '/trap/'})}

        assert actual == expected

    # No robot_txt found!
    def test_read_robot_txt_nonexistent(self):
        actual = read_robot_txt("https://lavenderpixl.github.io/#/robots.txt")
        expected = {'': (set(), set())}

        assert actual == expected

    # Testing with NO agent specified.
    def test_sort_robot_txt_none(self):
        robots_txt = test_get_robots_txt()
        actual = sort_allowed(None, robots_txt)
        expected = (
            {'/w/api.php?action=mobileview&', '/w/load.php?', '/api/rest_v1/?doc'},
            {'/w/', '/api/', '/trap/'})

        assert actual == expected

    # Testing with an agent in the Robots.txt
    def test_sort_robot_txt_single(self):
        robots_txt = test_get_robots_txt()
        actual = sort_allowed('*', robots_txt)
        expected = ({'/api/rest_v1/?doc', '/w/api.php?action=mobileview&', '/w/load.php?'},
                    {'/w/', '/api/', '/trap/'})

        assert actual == expected

    # Testing with agent NOT in Robots.txt
    def test_sort_robot_txt_wrong(self):
        robots_txt = test_get_robots_txt()
        actual = sort_allowed('tester', robots_txt)
        expected = ({'/api/rest_v1/?doc', '/w/api.php?action=mobileview&', '/w/load.php?'},
                    {'/w/', '/api/', '/trap/'})

        assert actual == expected


def test_get_html():
    f = open('testHtml.html', 'r')
    soup = BeautifulSoup(f, 'html.parser')
    f.close()
    return soup


class TestScraping(unittest.TestCase):
    def test_scrape_for_urls(self):
        actual = scrape_for_urls(test_get_html())
        expected = {'w/api.php?action=mobileview&', 'api/rest_v1/?doc', '/api/', '/w/'}

        assert actual == expected

    def test_check_urls(self):
        allowed, disallowed = {'w/api.php?action=mobileview&', 'api/rest_v1/?doc'}, {'/api/', '/w/'}
        # check_urls(test_get_html(), allowed, disallowed)


def create_csv_tester():
    f = ['Url', 'Domain', 'Allowed', 'Disallowed', 'Scraped']
    with open('temp.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(f)
        print("CSV tester created.")


def read_csv_tester():
    data_list = []

    with open('temp.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data_list.append(row)
    return data_list


def remove_csv_tester():
    file = 'temp.csv'
    if os.path.exists(file) and os.path.isfile(file):
        os.remove(file)
        print("CSV tester removed.")


class TestCSV(unittest.TestCase):
    def test_add_to_csv(self):
        site = website.Website("https://wikipedia.org", None, None, False)
        domains = [site]

        create_csv_tester()
        add_to_csv('temp.csv', domains)
        actual = read_csv_tester()
        remove_csv_tester()

        expected = [['Url', 'Domain', 'Allowed', 'Disallowed', 'Scraped'],
                    ['https://wikipedia.org wikipedia.org Null Null False']]

        assert actual == expected
