import sys
import uuid
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


"""
- https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
- https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker/
- https://stackoverflow.com/questions/52534658/webdriverexception-message-invalid-argument-cant-kill-an-exited-process-with
"""


def page_scroll_down(element, times):
    for _ in range(0, times):
        element.send_keys("", Keys.ARROW_DOWN)


def get_img_src(element):
    return element.get_attribute("src")


def print_img_src(element):
    print(get_img_src(element))


def download_img(element):
    src = get_img_src(element)
    id = str(uuid.uuid4())
    urlretrieve(src, f"media/{id}.jpg")


def find_all_images(wd):
    return wd.find_elements_by_xpath("//picture/img")


def main(wd, informed_number_of_times_to_scroll_down):
    body = driver.find_element_by_tag_name("body")
    page_scroll_down(
        body, informed_number_of_times_to_scroll_down)

    images = find_all_images(wd)
    for img in images:
        print_img_src(img)
        download_img(img)


def times_to_scroll_down_validation(informed_times):
    try:
        times = int(informed_times)
    except ValueError:
        raise ValueError("Enter numbers only.")

    if times < 0:
        raise Exception("Enter only nonnegative integers greater than zero.")

    return times


if __name__ == "__main__":
    informed_number_of_times_to_scroll_down = sys.argv[1]
    times = times_to_scroll_down_validation(
        informed_number_of_times_to_scroll_down)

    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get('http://9gag.com')

    main(driver, times)

    driver.close()
