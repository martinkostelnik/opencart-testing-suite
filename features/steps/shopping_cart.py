from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def get_driver(context):
    try:
        return context.browser
    except AttributeError:
        # context.browser = webdriver.Firefox("geckodriver-v0.26.0-win64")

        dp = {'browserName': 'firefox', 'marionette': 'true', 'javascriptEnabled': 'true'}
        context.browser = webdriver.Remote(
           command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
           desired_capabilities=dp)

    context.browser.implicitly_wait(10)

    return context.browser


@given("the shopping cart is empty")
def step_impl(context):
    context.browser = get_driver(context)
    context.browser.get("http://mys01.fit.vutbr.cz:8048/")


@when("the user opens the shopping cart")
def step_impl(context):
    context.browser.find_element(By.ID, "cart-total").click()


@then("message saying the shopping cart is empty is displayed")
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR, "li > .text-center").text == "Your shopping cart is empty!"
    context.browser.close()


@given("the web browser is at the OpenCart product page")
def step_impl(context):
    context.browser = get_driver(context)
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=product/product&product_id=43")


@when('the user clicks on the "Add to Cart" button on the right side of the page')
def step_impl(context):
    context.browser.find_element(By.ID, "button-cart").click()


@then("shopping cart contains the added item")
def step_impl(context):
    assert context.browser.find_element(By.LINK_TEXT, "MacBook").text == "MacBook"
    context.browser.close()


@given("the web browser is at the OpenCart shopping cart page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=checkout/cart")


@given("the shopping cart is not empty")
def step_impl(context):
    context.browser = get_driver(context)
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=product/product&product_id=43")
    context.browser.find_element(By.ID, "button-cart").click()
    assert context.browser.find_element(By.LINK_TEXT, "MacBook").text == "MacBook"


@when('the user clicks on the "Remove" button next to the quantity bar')
def step_impl(context):
    context.elemlen = len(context.browser.find_elements(By.CSS_SELECTOR, "tbody:nth-child(2) .text-center"))
    context.browser.find_element(By.CSS_SELECTOR, ".fa-times-circle").click()


@then("the item disappears from the shopping cart")
def step_impl(context):
    elements = context.browser.find_elements(By.CSS_SELECTOR, "tbody:nth-child(2) .text-center")
    assert len(elements) == context.elemlen - 1
    context.browser.close()


@given("a web browser is at OpenCart shopping cart page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=checkout/cart")


@when("the user enters a number into the quantity bar")
def step_impl(context):
    ch = ActionChains(context.browser)
    elem = context.browser.find_element(By.XPATH, "//div[@id=\'content\']/form/div/table/tbody/tr/td[4]/div/input")
    ch.double_click(elem).perform()
    elem.send_keys("42")
    elem.send_keys(Keys.ENTER)


@then("the prices displayed change accordingly")
def step_impl(context):
    assert float(context.browser.find_element(By.XPATH, "//div[@id=\'content\']/form/div/table/tbody/tr/td[6]").text[1:]) * 42 == 25284.00
    context.browser.close()


@when('the user click on the "Checkout" button')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Checkout").click()


@then('the "Checkout" page is displayed')
def step_impl(context):
    assert context.browser.title == "Checkout"
    context.browser.close()


@given('"Samsung Galaxy Tab 10.1" is out of stock')
def step_impl(context):
    pass


@when('user adds "Samsung Galaxy Tab 10.1" to the shopping cart')
def step_impl(context):
    context.browser = get_driver(context)
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=product/product&product_id=49")
    context.browser.find_element(By.ID, "button-cart").click()


@step("user navigates to the shopping cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=checkout/cart")


@then("a message 'Products marked with *** are not available in the desired quantity or not in stock!' is shown")
def step_impl(context):
    print("'" + context.browser.find_element(By.CSS_SELECTOR, ".alert-danger").text + "'")
    assert context.browser.find_element(By.CSS_SELECTOR, ".alert-danger").text == "Products marked with *** are not available in the desired quantity or not in stock!\n×"
    context.browser.close()