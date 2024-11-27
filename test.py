import unittest
from src.robotTxt import *


def test_get_robots_txt():
    conn = open("testRobotTxt.txt", "r")
    robots_txt = conn.read()
    conn.close()
    result = read_robot_txt(robots_txt)
    return result


class TestRobotTxt(unittest.TestCase):

    def test_read_robot_txt(self):
        result = test_get_robots_txt()
        assert result == {'k2spider': (set(), {'/'}), 'NPBot': (set(), {'/'}), '*': (
            {'/api/rest_v1/?doc', '/w/load.php?', '/w/api.php?action=mobileview&'}, {'/api/', '/w/', '/trap/'})}

    def test_sort_robot_txt_none(self):
        robots_txt = test_get_robots_txt()
        none = sort_allowed([], robots_txt)
        assert none == (set(), set())

    def test_sort_robot_txt_single(self):
        robots_txt = test_get_robots_txt()
        single = sort_allowed(['k2spider'], robots_txt)
        print(single)
        assert single == (set(), set('/'))

    def test_sort_robot_txt_multiple(self):
        robots_txt = test_get_robots_txt()
        actual = sort_allowed(['*', 'k2spider', 'tester'], robots_txt)
        expected = (
            {'/api/rest_v1/?doc', '/w/api.php?action=mobileview&', '/w/load.php?'},
            {'/w/', '/api/', '/', '/trap/'}
        )

        print(actual, expected)
        assert actual == expected
