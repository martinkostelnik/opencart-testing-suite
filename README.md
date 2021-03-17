## eCommerce OpenCart testing suite

---

The task was to create BDD testing scenarios for different parts of eCommerce OpenCart using Cucumber and later implement them using python. I selected three parts and created a few scenarios describing their behaviour. The selected parts are shopping cart, customer management and review system.

### shopping_cart.feature

This file desribes the behaviour of the shopping car and is implemented from a customer's point of view. The scenarios aim to test basic funcionality, such as:
- adding products
- removing products
- checkout page
- modifying quantity

### admin_customers.feature

Here we take a look at a behaviour from administrator's point of view. These tests cover the management and filtering of customer accounts.

### reviews.feature

Behaviour from both administrator's and user's point of view. Submitting a proper review and a invalid review is described. Administrator then tests approving new review, deleting and modyfying an existing one.