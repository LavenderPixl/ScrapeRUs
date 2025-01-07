import unittest
from src.robotTxt import *


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
            {'/api/rest_v1/?doc', '/w/load.php?', '/w/api.php?action=mobileview&'}, {'/api/', '/w/', '/trap/'})}

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
            {'/w/api.php?action=mobileview&', '/w/load.php?', '/api/rest_v1/?doc'}, {'/w/', '/api/', '/trap/'})

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
