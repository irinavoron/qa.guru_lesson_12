from selene import browser, by, have


def test_github_issue():
    browser.open('/')
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('irinavoron/qa.guru_lesson_12').press_enter()
    browser.element(by.link_text('irinavoron/qa.guru_lesson_12')).click()
    browser.element('#issues-tab').click()
    browser.element('[aria-label=Issues][role=group]').should(have.text('Issue created for the homework'))
