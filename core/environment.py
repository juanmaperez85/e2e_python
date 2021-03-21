import ConfigParser
import os
import time
from datetime import datetime

from core.utils import get_driver_path
from django.conf import settings
from pyvirtualdisplay import Display
from selenium import webdriver


def before_all(context):
    context.config = ConfigParser.RawConfigParser()
    context.config.read(os.getcwd() + settings.PROPERTIES_PATH)
    # displaying test execution in a browser
    # change to visible = 1 if necessary
    context.display = Display(visible=1, size=(1620, 1080))
    context.scenario_start_time = datetime.now()
    context.display.start()


def before_scenario(context, scenario):
    time.sleep(0.1)
    # Clear the data we are using to store variables to be used along the steps
    context.data = {}
    chromedriver = get_driver_path()
    os.environ["webdriver.chrome.driver"] = chromedriver
    context.browser = webdriver.Chrome(chromedriver)  # add new setting to choose the webdriver?
    context.browser.implicitly_wait(10)
    context.browser.set_window_size(1920, 1080)
    context.browser.set_window_position(0, 0)
    context.browser.implicitly_wait(10)
    scenario.scenario_start_time = datetime.now()


def after_step(context, step):
    time.sleep(0.1)
    if hasattr(context, 'lp') and step.name != "nothing is done until all ajax have finished":
        context.execute_steps(u"""
            When nothing is done until all ajax have finished
       """)


def after_scenario(context, scenario):
    time.sleep(0.1)
    # Clear the data we are using to store variables to be used along the steps
    context.data = {}
    context.browser.quit()
    scenario.scenario_end_time = datetime.now()
    scenario.scenario_duration_time = scenario.scenario_end_time - scenario.scenario_start_time
    print(
        "After_scenario {} start_time: {} end_time: {} duration_time: {} seconds".format(
            scenario,
            scenario.scenario_start_time,
            scenario.scenario_end_time,
            scenario.scenario_duration_time.total_seconds()
        )
    )


def after_all(context):
    context.scenario_end_time = datetime.now()
    context.scenario_duration_time = context.scenario_end_time - context.scenario_start_time
    print(
        "After_all {} start_time: {} end_time: {} duration_time: {} seconds".format(
            context,
            context.scenario_start_time,
            context.scenario_end_time,
            context.scenario_duration_time.total_seconds()
        )
    )
    context.display.stop()
