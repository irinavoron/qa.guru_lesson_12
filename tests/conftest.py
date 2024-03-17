import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1896
    browser.config.window_height = 1080

    yield

    browser.quit()
