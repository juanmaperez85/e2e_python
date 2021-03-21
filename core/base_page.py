from __future__ import unicode_literals

from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support.expected_conditions import (
    _element_if_visible,
    _find_elements
)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class visibility_of_all_elements_located(object):
    """ An expectation for checking that all elements are present on the DOM of a
    page and visible. Visibility means that the elements are not only displayed
    but also have a height and width that is greater than 0.
    locator - used to find the element
    returns the list of WebElement once they are located and visible
    """

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            elements = _find_elements(driver, self.locator)
            visible_elements = []
            for e in elements:
                element_visible = _element_if_visible(e)
                if element_visible:
                    visible_elements.append(element_visible)
            return visible_elements if len(visible_elements) > 0 and len(visible_elements) == len(elements) else False
        except StaleElementReferenceException:
            return False


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser

    def goto(self, context):
        return context.browser.get(self.get_base_url(context) + self.url)

    # press the element with the id passed
    def press_button(self, element):
        self.button = self.browser.find_element_by_css_selector(getattr(self, element))
        self.button.click()

    def press_button_xpath(self, element):
        self.button = self.browser.find_element_by_xpath(getattr(self, element))
        self.button.click()

    # should pass an element id and a value, and will fill the element with the value passed
    def complete_field(self, element, value):
        # self.field = self.browser.find_element_by_css_selector(getattr(self, element))
        field = self.wait_for_visible_element(getattr(self, element))
        field.clear()
        field.send_keys(value)

        return field

    def check_exist_element(self, element):
        try:
            return True if self.wait_for_visible_element(getattr(self, element)) else False
        except TimeoutException:
            return False

    def wait_for_element(self, css_selector, seconds=10):
        element = WebDriverWait(self.browser, seconds).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    # wait a maximun of the seconds passed to the element with the css passed
    def wait_for_visible_element(self, css_selector, seconds=10):
        element = WebDriverWait(self.browser, seconds).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    def wait_until_ajax_complete(self):
        try:
            WebDriverWait(self.browser, 10 * 60).until(
                AjaxCallsObserver(self.browser)
            )
        except WebDriverException:
            pass

    def wait_until_page_is_requested(self):
        try:
            WebDriverWait(self.browser, 2*60).until(
                AboutBlankObserver(self.browser)
            )
        except WebDriverException:
            pass

    def scroll_to_element(self, el_selector):
        script_str = 'scroll(0, $("{}").offset().top-200);'.format(el_selector)
        self.browser.execute_script(script_str)

    def get_text(self, element):
        from core.utils import sleep
        max_attempts = 10
        attempt = 1
        obtained = False
        exception = None
        while attempt <= max_attempts and not obtained:
            try:
                text_value = self.wait_for_visible_element(getattr(self, element)).text
                obtained = True
                return text_value
            except (StaleElementReferenceException, TimeoutException) as e:
                sleep(1)
                exception = e
            attempt += 1
        if not obtained:
            if exception:
                raise exception
            else:
                raise Exception("it has not been possible to get the text of the element")


class AjaxCallsObserver(object):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, driver):
        return driver.execute_script("return jQuery.active == 0")


class AboutBlankObserver(object):
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, driver):
        return driver.current_url != "about:blank"