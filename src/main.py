import robotTxt
import scrape

if __name__ == '__main__':
    urls = ['https://lavenderpixl.github.io']

    robot_txt = robotTxt.setup_robot_txt(urls)
    print(f"Allowed: {robot_txt[0]}")
    print(f"Disallowed: {robot_txt[1]}")
