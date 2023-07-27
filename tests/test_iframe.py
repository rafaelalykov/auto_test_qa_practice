from pages.iframe import Iframe

def test_iframe_page(browser):
    iframe_page = Iframe(browser)
    iframe_page.open()
    iframe_page.iframe()
    browser.switch_to.frame(0)
    iframe_page.click_contact()
    assert "Album example" == iframe_page.check_text().text