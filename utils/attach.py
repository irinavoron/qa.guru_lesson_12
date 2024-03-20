import os
import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, 'screenshot', AttachmentType.PNG, '.png')


def add_logs(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'html', AttachmentType.HTML, '.html')


def add_video(browser):
    url = os.getenv('SELENOID_URL')
    video_url = f'https://{url}video/' + browser.driver.session_id + '.mp4'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')
