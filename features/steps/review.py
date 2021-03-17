from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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


@given("the user navigated to reviews page of a specific product")
def step_impl(context):
    context.browser = get_driver(context)
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=product/product&product_id=43")
    context.browser.find_element(By.LINK_TEXT, "Reviews (1)").click()


@when("the user properly filled all the fields")
def step_impl(context):
    context.browser.find_element(By.ID, "input-name").click()
    context.browser.find_element(By.ID, "input-name").send_keys("Martin Novnot7")
    context.browser.find_element(By.ID, "input-review").send_keys("Nejlepsi review je tato review")
    context.browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()


@step('the user clicked on "continue" button')
def step_impl(context):
    context.browser.find_element(By.ID, "button-review").click()


@then('a message "Thank you for your review. It has been submitted to the webmaster for approval." is shown')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR,
        ".alert").text == "Thank you for your review. It has been submitted to the webmaster for approval."
    context.browser.close()


@when('the user enters a review shorter than "25" characters')
def step_impl(context):
    context.browser.find_element(By.ID, "input-name").click()
    context.browser.find_element(By.ID, "input-name").send_keys("Martin Novnot7")
    context.browser.find_element(By.ID, "input-review").send_keys("kratka review")
    context.browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()
    context.browser.find_element(By.ID, "button-review").click()


@then('an error message "Warning: Review Text must be between 25 and 1000 characters!" is shown')
def step_impl(context):
    assert context.browser.find_element(By.CSS_SELECTOR,
        ".alert").text == "Warning: Review Text must be between 25 and 1000 characters!"
    context.browser.close()


@given("the admin navigated to Reviews page in the admin area")
def step_impl(context):
    context.browser = get_driver(context)
    context.browser.get("http://mys01.fit.vutbr.cz:8048/admin/")
    context.browser.find_element(By.ID, "input-username").click()
    context.browser.find_element(By.ID, "input-username").send_keys("admin")
    context.browser.find_element(By.ID, "input-password").click()
    context.browser.find_element(By.ID, "input-password").send_keys("admin")
    context.browser.find_element(By.CSS_SELECTOR, ".fa-key").click()
    element = context.browser.find_element(By.CSS_SELECTOR, "#catalog > .parent")
    actions = ActionChains(context.browser)
    actions.move_to_element(element).perform()
    context.browser.find_element(By.LINK_TEXT, "Reviews").click()
    context.browser.close()


@given('a review for "iPhone" was submitted')
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8048/index.php?route=product/product&product_id=40")
    context.browser.find_element(By.LINK_TEXT, "Reviews (1)").click()
    context.browser.find_element(By.ID, "input-name").click()
    context.browser.find_element(By.ID, "input-name").send_keys("ajfon review je zde a je super")
    context.browser.find_element(By.ID, "input-review").send_keys("Nejlepsi review je tato review")
    context.browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)").click()
    context.browser.find_element(By.ID, "button-review").click()



@step('a review for "iPhone" is not approved')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a review for "iPhone" is not approved')


@when("the admin changes status from disabled to enabled")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the admin changes status from disabled to enabled')


@then('the approved review is shown on "iPhone" reviews page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the approved review is shown on "iPhone" reviews page')


@given('an approved review for "iPhone" exists')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And an approved review for "iPhone" exists')


@when('admin selects a review for "iPhone"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When admin selects a review for "iPhone"')


@step('the admin clicks on the "Delete" button in the upper right corner on review screen')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the admin clicks on the "Delete" button in the upper right corner')


@then('an "iPhone" review is no longer in the reviews list')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then an "iPhone" review is no longer in the reviews list')


@step('the deleted review is not present on the "iPhone" reviews page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the deleted review is not present on the "iPhone" reviews page')


@given('the admin navigated to the Edit Review page of "iPhone" review')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the admin navigated to the Edit Review page of "iPhone" review')


@when('the admin changes product to "MacBook"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the admin changes product to "MacBook"')


@then('the edited review is not present on the "iPhone" reviews page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the edited review is not present on the "iPhone" reviews page')


@step('the edited review is present on the "MacBook" reviews page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the edited review is present on the "MacBook" reviews page')
