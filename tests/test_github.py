import allure
from selene import browser, by, have


@allure.label('owner', 'irinavoron')
@allure.feature('Issues tab')
@allure.story('Issue with the indicated text in the title should be displayed on the page')
@allure.title('Issue with the indicated text in the title should be displayed on the page')
def test_github_issues():
    allure.dynamic.link('https://github.com/')

    with allure.step('Open main page'):
        browser.open('/')

    with allure.step('Search for repository'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type('irinavoron/qa.guru_lesson_12').press_enter()

    with allure.step('Go to the repository'):
        browser.element(by.link_text('irinavoron/qa.guru_lesson_12')).click()

    with allure.step('Open the Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('The issue with the text in title should be displayed on the page'):
        browser.element('[aria-label=Issues][role=group]').should(have.text('Issue created for the homework'))
