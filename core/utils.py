import os
import time


def get_driver_path(driver='chromedriver'):
    default_chromedriver_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'drivers', driver)

    return os.environ.get('CHROMEDRIVER_PATH', default_chromedriver_path)


def sleep(seconds):
    if isinstance(seconds, int) or isinstance(seconds, float):
        if seconds > 30:
            seconds = 30
        timeout = time.time() + seconds
        while time.time() < timeout:
            pass
    else:
        raise Exception("{} is not a number".format(seconds))


def get_settings():
    settings = os.environ.get("DJANGO_SETTINGS_MODULE")
    setting = settings.split(".")
    return setting[2]
