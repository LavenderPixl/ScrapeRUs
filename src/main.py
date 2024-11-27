import robotTxt
import scrape

if __name__ == '__main__':
    urls = ['https://en.wikipedia.org']
    my_agents = ['*', 'LavSpidey']

    robot_txt = robotTxt.setup_robot_txt(my_agents, urls)
    # test = robotTxt.check_request('https://en.wikipedia.org')
    # print(test)
    # print(robot_txt)
