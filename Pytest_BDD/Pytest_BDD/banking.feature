Feature: Banking Application
  In order to manage my finances
  As a user
  I want to be able to transfer funds between my accounts
 
  Scenario: Transfer funds between accounts
    Given I have an account with balance $1000
    And I have another account with balance $500
    When I transfer $300 from the first account to the second account
    Then the balance of the first account should be $700
    And the balance of the second account should be $800