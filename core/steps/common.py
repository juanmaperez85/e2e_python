import time

from behave import (
    given,
    when,
    then,
    step,
)
from nose.tools import assert_in

from core.pages import get_page_class


@given('log in with the configured user')
def login_user_password(context):
    # Username and password set in properties.cfg
    user = context.config.get('PACKLINK', 'USERNAME')
    password = context.config.get('PACKLINK', 'PASSWORD')
    context.execute_steps(u"""
        When I go to "Login Page"
        And I press cookie button "confirm_cookies" in "Login Page"
        And I fill "username" with "{0}" in "Login Page"
        And I fill "password" with "{1}" in "Login Page"
        And I press button "login_button" in "Login Page"
    """.format(user, password))


@when('I go to "{page}"')
def access_page(context, page):
    page_class = get_page_class(page)
    page = page_class(context.browser)
    page.goto(context)
    context.browser.implicitly_wait(1)


@when('I fill "{element}" with "{value}" in "{page}"')
def fill_element_with_value(context, element, value, page):
    page_class = get_page_class(page)
    context.lp = page_class(context.browser)
    context.lp.complete_field(element, value)


@when('I press button "{element}" in "{page}"')
def press_button(context, element, page):
    page_class = get_page_class(page)
    context.lp = page_class(context.browser)
    context.lp.press_button(element)
    context.lp.wait_until_page_is_requested()
    context.lp.wait_until_ajax_complete()
    time.sleep(int(1))

@when('I press cookie button "{element}" in "{page}"')
@when('I press xpath button "{element}" in "{page}"')
def press_button_xpath(context, element, page):
    page_class = get_page_class(page)
    context.lp = page_class(context.browser)
    context.lp.press_button_xpath(element)
    context.lp.wait_until_ajax_complete()


@then('the "{element}" element is displayed in "{page_class}"')
def check_element(context, element, page_class):
    page = get_page_class(page_class)
    context.lp = page(context.browser)
    result = context.lp.check_exist_element(element)
    assert True == result, "The element {0} does not appear in {1}".format(element, page_class)


@step('I wait for "{seconds}" seconds')
def wait_seconds(context, seconds):
    time.sleep(int(seconds))


@step('nothing is done until all ajax have finished')
def wait_ajax(context):
    context.lp.wait_until_ajax_complete()


@when('the page is scrolled to element "{element}" on the page "{page}"')
def page_is_scrolled_step_impl(context, element, page):
    """ Scrolls to an element in the page. """
    page_class = get_page_class(page)
    context.page = page_class(context.browser)
    el_selector = getattr(page_class, element)
    context.page.scroll_to_element(el_selector)


@then('I should see the text "{value}" in the container "{element}" of the page "{page}"')
def should_see_text_step_impl(context, value, element, page):
    from core.utils import sleep
    max_attempts = 10
    attempt = 1
    checked = False
    exception = None
    error_message = ""
    while attempt <= max_attempts and not checked:
        try:
            page_class = get_page_class(page)
            context.lp = page_class(context.browser)
            text = context.lp.get_text(element)
            error_message = "{0} does not contains the value '{1}': '{2}'".format(element, value, text)
            assert_in(value, text, error_message)
            checked = True
        except AssertionError as e:
            sleep(1)
            exception = e
        attempt += 1
    if not checked:
        if exception:
            raise exception
        else:
            raise Exception(error_message)
