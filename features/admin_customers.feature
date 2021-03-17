# -- FILE: admin_customers.feature

Feature: Customer management

    Background:
        Given the following users exist
            | name          | e-mail                |
            | Jan Novotny   | jannovotny@gmail.com  |
            | Josef Stary   | josefstary@gmail.com  |
            | Daniel Mlady  | danielmlady@seznam.cz |

    Scenario: Add a customer
        Given the admin navigated to Add customer page
        When admin creates a customer called "Martin Raska" with "martinraska@gmail.com" e-mail
        Then a customer called "Martin Raska" with "martinraska@gmail.com" e-mail is present in the customer list

    Scenario: Delete a customer
        Given the admin navigated to Customers page
        When admin selects a customer called "Jan Novotny" with "jannovotny@gmail.com" e-mail
        And the admin clicks on the "Delete" button in the upper right corner
        Then a customer called "Jan Novotny" with "jannovotny@gmail.com" e-mail is not present in the customer list

    Scenario: Change a customer's name
        Given the admin is logged in as "Jan Novotny"
        And the admin navigated to Edit information page
        When the admin enters "Honza" into the First Name field
        Then the customer's name is "Honza Novotny"

    Scenario: Find an existing customer
        Given the admin navigated to Customers page
        When the admin enters "Josef Stary" into the Customer Name bar
        Then the customers called "Josef Stary" are the only ones present in customer list

    Scenario: Create a Customer group
        Given the admin navigated to Add Customer Group page
        When the admin creates a group called "Stamgasti"
        Then the customer group called Stamgasti exists

    Scenario: Add customer to customer group
        Given a customer group called "Stamgasti" exists
        When admin changes customer group of "Daniel Mlady" to "Stamgasti"
        Then customer "Daniel Mlady" is present among members of "Stamgasti"
