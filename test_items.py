link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_all_languages(browser):
    browser.get(link)
    # x = browser.find_element_by_class_name("btn-add-to-basket")
    # assert x is not None, 'СООБЩЕНИЕ'
    assert "btn-add-to-basket1" in browser.page_source, 'СООБЩЕНИЕ'

