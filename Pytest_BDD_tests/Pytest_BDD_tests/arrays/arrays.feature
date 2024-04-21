Feature: Array Operations

  Scenario: Initialize an empty array
    Given a new array
    Then the array should be empty

  Scenario: Append an item to the array
    Given a new array
    When I append 1 to the array
    Then the array should not be empty

  Scenario: Remove an item from the array
    Given a new array
    And I append 1 to the array
    When I remove 1 from the array
    Then the array should be empty

  Scenario: Get item at a specific index
    Given a new array
    And I append 1 to the array
    And I append 2 to the array
    When I get item at index 0
    Then it should be 1
    When I get item at index 1
    Then it should be 2

  Scenario: Get item at an invalid index
    Given a new array
    When I get item at index 0
    Then it should be None

  Scenario: Check the size of the array
    Given a new array
    And I append 1 to the array
    And I append 2 to the array
    When I remove 1 from the array
    Then the size of the array should be 1
    When I remove 2 from the array
    Then the size of the array should be 0
