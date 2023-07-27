from base_page import BasePage
from selenium.webdriver.common.by import By

box_one_selector = (By.ID, 'rect-draggable')
box_two_selector = (By.ID, 'rect-droppable')
check_result = (By.ID, "text-droppable")

class DragAndDropBoxes(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/dragndrop/boxes")

    def box_one(self):
        return self.find(box_one_selector)

    def box_two(self):
        return self.find(box_two_selector)

    def result(self):
        return self.find(check_result)

image_one_selector = (By.ID, "rect-droppable1")
image_two_selector = (By.ID, "rect-droppable2")
check_images_result = (By.XPATH, "//p[@class='text-droppable']")


class DragAndDropImages(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get("https://www.qa-practice.com/elements/dragndrop/images")

    def image_one(self):
        return self.find(image_one_selector)

    def image_two(self):
        return self.find(image_two_selector)

    def result(self):
        return self.find(check_images_result)