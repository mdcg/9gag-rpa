import sys
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from db.connection import Connection


"""
- https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
- https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker/
- https://stackoverflow.com/questions/52534658/webdriverexception-message-invalid-argument-cant-kill-an-exited-process-with
"""


class BOT(object):
    def __init__(self, wd, times_to_scroll_down):
        self.wd = wd
        self.times_to_scroll_down = self.times_to_scroll_down_validation(
            times_to_scroll_down)
        self.conn = Connection()
        self.wd.get('http://9gag.com')

    def page_scroll_down(self, element, times):
        for _ in range(0, times):
            element.send_keys("", Keys.ARROW_DOWN)

    def get_img_src(self, element):
        return element.get_attribute("src")

    def get_img_name(self, src):
        return src.split("/")[-1]

    def print_img_src(self, element):
        print(self.get_img_src(element))

    def download_img(self, element):
        src = self.get_img_src(element)
        img_name = self.get_img_name(src)

        if self.conn.img_name_already_exists_in_db(img_name):
            return

        self.conn.insert_img_name_in_db(img_name)
        urlretrieve(src, f"media/{img_name}")

    def find_all_images(self):
        return self.wd.find_elements_by_xpath("//picture/img")

    def start(self):
        body = self.wd.find_element_by_tag_name("body")
        self.page_scroll_down(
            body, self.times_to_scroll_down)

        images = self.find_all_images()
        for img in images:
            self.print_img_src(img)
            self.download_img(img)

        self.conn.close_connection()

    def times_to_scroll_down_validation(self, informed_times):
        try:
            times = int(informed_times)
        except ValueError:
            raise ValueError("Enter numbers only.")

        if times < 0:
            raise Exception(
                "Enter only nonnegative integers greater than zero.")

        return times


if __name__ == "__main__":
    try:
        informed_number_of_times_to_scroll_down = sys.argv[1]
    except IndexError:
        raise IndexError(
            "You need to enter the number of times you want to scroll down. e.g. python app.py 1000")

    options = Options()
    options.headless = True
    wdriver = webdriver.Firefox(options=options)

    rpa_bot = BOT(wdriver, informed_number_of_times_to_scroll_down)
    rpa_bot.start()

    wdriver.close()
