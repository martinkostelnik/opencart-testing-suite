# -- FILE: shopping_cart.feature

Feature: Shopping cart

    Scenario: Open empty shopping cart
        Given the shopping cart is empty
        When the user opens the shopping cart
        Then message saying the shopping cart is empty is displayed

    Scenario: Add a product to the shopping cart
        Given the web browser is at the OpenCart product page
        When the user clicks on the "Add to Cart" button on the right side of the page
        Then shopping cart contains the added item

    Scenario: Remove a product from shopping cart
        Given the shopping cart is not empty
        And the web browser is at the OpenCart shopping cart page
        When the user clicks on the "Remove" button next to the quantity bar
        Then the item disappears from the shopping cart

    Scenario: Change the quantity of an item in the shopping cart
        Given the shopping cart is not empty
        And a web browser is at OpenCart shopping cart page
        When the user enters a number into the quantity bar
        Then the prices displayed change accordingly

    Scenario: Get to checkout page
        Given the shopping cart is not empty
        And a web browser is at OpenCart shopping cart page
        When the user click on the "Checkout" button
        Then the "Checkout" page is displayed

    Scenario: Buying out of stock product
        Given "Samsung Galaxy Tab 10.1" is out of stock
        When user adds "Samsung Galaxy Tab 10.1" to the shopping cart
        And user navigates to the shopping cart
        Then a message 'Products marked with *** are not available in the desired quantity or not in stock!' is shown
