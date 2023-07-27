from selenium.webdriver import Keys
from pages.word_input import WordInput

def test_word_input(browser):
    word_input = WordInput(browser)
    word = 'python'
    word_input.open()
    string = word_input.string()
    string.send_keys(word)
    string.send_keys(Keys.RETURN)
    assert word == word_input.result()

def test_text_input_not_valid(browser):
    word_input = WordInput(browser)
    text = 'python 1'
    word_input.open()
    string = word_input.string()
    string.send_keys(text)
    string.send_keys(Keys.RETURN)
    assert word_input.value_warring()