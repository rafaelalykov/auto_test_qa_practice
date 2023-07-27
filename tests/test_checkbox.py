from pages.checkbox import CheckBoxSingle, CheckBoxMult

def test_single_checkbox(browser):
    single_checkbox = CheckBoxSingle(browser)
    single_checkbox.open()
    single_checkbox.click_box()
    single_checkbox.click_button()
    assert 'select me or not' == single_checkbox.result().text

def test_one_checkbox(browser):
    mult_checkbox = CheckBoxMult(browser)
    mult_checkbox.open()
    mult_checkbox.click_box2()
    mult_checkbox.click_submit_button()
    assert "two" == mult_checkbox.result().text

def test_two_checkbox(browser):
    mult_checkbox = CheckBoxMult(browser)
    mult_checkbox.open()
    mult_checkbox.click_box1()
    mult_checkbox.click_box2()
    mult_checkbox.click_submit_button()
    assert "one, two" == mult_checkbox.result().text

def test_three_checkbox(browser):
    mult_checkbox = CheckBoxMult(browser)
    mult_checkbox.open()
    mult_checkbox.click_box1()
    mult_checkbox.click_box2()
    mult_checkbox.click_box3()
    mult_checkbox.click_submit_button()
    assert 'one, two, three' == mult_checkbox.result().text
