# -- FILE: review.feature

Feature: Review submitting and management

    Scenario: Submit a review
        Given the user navigated to reviews page of a specific product
        When the user properly filled all the fields
        And the user clicked on "continue" button
        Then a message "Thank you for your review. It has been submitted to the webmaster for approval." is shown

    Scenario: Review length is below limit
        Given the user navigated to reviews page of a specific product
        When the user enters a review shorter than "25" characters
        Then an error message "Warning: Review Text must be between 25 and 1000 characters!" is shown
    
    Scenario: Approve a review
        Given a review for "iPhone" was submitted
        And the admin navigated to Reviews page in the admin area
        And a review for "iPhone" is not approved
        When the admin changes status from disabled to enabled
        Then the approved review is shown on "iPhone" reviews page

    Scenario: Delete a review
        Given the admin navigated to Reviews page in the admin area
        And an approved review for "iPhone" exists
        When admin selects a review for "iPhone"
        And the admin clicks on the "Delete" button in the upper right corner on review screen
        Then an "iPhone" review is no longer in the reviews list
        And the deleted review is not present on the "iPhone" reviews page

    Scenario: Edit a review
        Given an approved review for "iPhone" exists
        And the admin navigated to the Edit Review page of "iPhone" review
        When the admin changes product to "MacBook"
        Then the edited review is not present on the "iPhone" reviews page
        And the edited review is present on the "MacBook" reviews page
