import unittest
from src.robotTxt import *


def setup_robot_txt():
    conn = open("testRobotTxt.txt", "r")
    robots_txt = conn.read()
    conn.close()
    result = read_robot_txt(robots_txt)
    return result


class TestRobotTxt(unittest.TestCase):

    def test_read_robot_txt(self):
        result = setup_robot_txt()
        print(result)

        assert result == {'k2spider': (set(), {'/'}), 'NPBot': (set(), {'/'}), '*': (
        {'/api/rest_v1/?doc', '/w/load.php?', '/w/api.php?action=mobileview&'}, {'/api/', '/w/', '/trap/'})}

