Feature: Stack operations

  Scenario: Push and pop items
    Given an empty stack
    When I push an item 5
    Then the stack should have 1 item
    And the popped item should be 5