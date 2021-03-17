from behave import *

@given("the following users exist")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the following users exist ')


@given("the admin navigated to Add customer page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the admin navigated to Add customer page')


@when('admin creates a customer called "Martin Raska" with "martinraska@gmail\.com" e-mail')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: When admin creates a customer called "Martin Raska" with "martinraska@gmail.com" e-mail')


@then('a customer called "Martin Raska" with "martinraska@gmail\.com" e-mail is present in the customer list')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then a customer called "Martin Raska" with "martinraska@gmail.com" e-mail is present in the customer list')


@given("the admin navigated to Customers page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the admin navigated to Customers page')


@when('admin selects a customer called "Jan Novotny" with "jannovotny@gmail\.com" e-mail')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: When admin selects a customer called "Jan Novotny" with "jannovotny@gmail.com" e-mail')


@then('a customer called "Jan Novotny" with "jannovotny@gmail\.com" e-mail is not present in the customer list')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then a customer called "Jan Novotny" with "jannovotny@gmail.com" e-mail is not present in the customer list')


@given('the admin is logged in as "Jan Novotny"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the admin is logged in as "Jan Novotny"')


@step("the admin navigated to Edit information page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the admin navigated to Edit information page')


@when('the admin enters "Honza" into the First Name field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the admin enters "Honza" into the First Name field')


@then('the customer\'s name is "Honza Novotny"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the customer\'s name is "Honza Novotny"')


@when('the admin enters "Josef Stary" into the Customer Name bar')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the admin enters "Josef Stary" into the Customer Name bar')


@then('the customers called "Josef Stary" are the only ones present in customer list')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then the customers called "Josef Stary" are the only ones present in customer list')


@given("the admin navigated to Add Customer Group page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the admin navigated to Add Customer Group page')


@when('the admin creates a group called "Stamgasti"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the admin creates a group called "Stamgasti"')


@then("the customer group called Stamgasti exists")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the customer group called Stamgasti exists')


@given('a customer group called "Stamgasti" exists')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given a customer group called "Stamgasti" exists')


@when('admin changes customer group of "Daniel Mlady" to "Stamgasti"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When admin changes customer group of "Daniel Mlady" to "Stamgasti"')


@then('customer "Daniel Mlady" is present among members of "Stamgasti"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then customer "Daniel Mlady" is present among members of "Stamgasti"')
