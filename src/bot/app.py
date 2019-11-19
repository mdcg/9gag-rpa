from selenium import webdriver
from selenium.webdriver.firefox.options import Options


"""
- https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path
- https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker/
- https://stackoverflow.com/questions/52534658/webdriverexception-message-invalid-argument-cant-kill-an-exited-process-with
"""

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('http://9gag.com')

img_contents = driver.find_elements_by_tag_name('img')

for img in img_contents:
    print(img.get_attribute("src"))
    # driver.find_element_by_id(img.get_attribute("id")).click()

assert "9GAG" in driver.title
