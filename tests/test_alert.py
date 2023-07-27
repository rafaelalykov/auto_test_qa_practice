from pages.alert import AlertBox, AlertConferm, AlertPromt

def test_alert_box(browser):
    alert_box = AlertBox(browser)
    alert_box.open()
    alert_box.click_button()
    assert alert_box.ok_push

def test_alert_conferm_ok(browser):
    alert_conferm = AlertConferm(browser)
    alert_conferm.open()
    alert_conferm.click_button()
    alert_conferm.switch_to_alert_accept()
    assert "Ok" == alert_conferm.result().text

def test_alert_conferm_cancel(browser):
    alert_conferm = AlertConferm(browser)
    alert_conferm.open()
    alert_conferm.click_button()
    alert_conferm.switch_to_alert_dismiss()
    assert "Cancel" == alert_conferm.result().text

def test_alert_prompt_accept(browser):
    alert_promt = AlertPromt(browser)
    alert_promt.open()
    alert_promt.click_button()
    browser.switch_to.alert.send_keys("Hello Python")
    alert_promt.assept_alert()
    assert "Hello Python" == alert_promt.result().text

def test_alert_prompt_clear_accept(browser):
    alert_promt = AlertPromt(browser)
    alert_promt.open()
    alert_promt.click_button()
    browser.switch_to.alert.send_keys('')
    alert_promt.assept_alert()
    assert "You entered nothing" == alert_promt.result().text

def test_alert_prompt_dismiss(browser):
    alert_promt = AlertPromt(browser)
    alert_promt.open()
    alert_promt.click_button()
    alert_promt.dismiss_alert()
    assert "You canceled the prompt" == alert_promt.result().text