from pages.new_tab import NewTabLink, NewTabButton

def test_new_tab_link(browser):
    tab_link = NewTabLink(browser)
    tab_link.open()
    tab_link.click_link_button()
    browser.switch_to.window(browser.window_handles[1])
    assert "I am a new page in a new tab" == tab_link.result().text

def test_new_tab_button(browser):
    tab_button = NewTabButton(browser)
    tab_button.open()
    tab_button.click_button()
    browser.switch_to.window(browser.window_handles[1])
    assert "I am a new page in a new tab" == tab_button.result().text