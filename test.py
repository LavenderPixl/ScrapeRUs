import unittest
from src.robotTxt import *

class TestRobotTxt(unittest.TestCase):

    def test_read_robot_txt(self):
        current_agent = ["*"]
        conn = open("testRobotTxt.txt", "r")
        robots_txt = conn.read()
        conn.close()
        result = read_robot_txt(current_agent, robots_txt)
        print(result)

        assert result == {'k2spider': (set(), {'/'}), 'NPBot': (set(), {'/'}), '*': ({'/api/rest_v1/?doc', '/w/load.php?', '/w/api.php?action=mobileview&'}, {'/api/', '/w/', '/trap/'})}


