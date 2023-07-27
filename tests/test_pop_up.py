from pages.pop_up import PopUp

def test_pop_up_modal(browser):
    pop_up = PopUp(browser)
    pop_up.open()
    pop_up.click_launch()
    pop_up.click_check_box()
    pop_up.click_send_button()
    assert 'select me or not' == pop_up.result().text

