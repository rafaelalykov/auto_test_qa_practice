from selenium.webdriver import ActionChains
from pages.dragndrop import DragAndDropBoxes, DragAndDropImages

def test_dragndrop_boxex(browser):
    dragndrop = DragAndDropBoxes(browser)
    dragndrop.open()
    box1 = dragndrop.box_one()
    box2 = dragndrop.box_two()
    ActionChains(browser).drag_and_drop(box1, box2).perform()
    assert 'Dropped!' == dragndrop.result().text

def test_dragndrop_images(browser):
    dragndrop = DragAndDropImages(browser)
    dragndrop.open()
    image1 = dragndrop.image_one()
    image2 = dragndrop.image_two()
    ActionChains(browser).drag_and_drop(image1, image2).perform()
    ActionChains(browser).drag_and_drop(image2, image1).perform()
    assert 'Dropped!' == dragndrop.result().text