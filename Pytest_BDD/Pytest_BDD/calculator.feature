Feature: Calculator operations

  Scenario: Add two numbers
    Given a calculator
    When I add 5 and 7
    Then the result should be 12

  Scenario: Subtract two numbers
    Given a calculator
    When I subtract 7 from 12
    Then the result should be 5

  Scenario: Multiply two numbers
    Given a calculator
    When I multiply 4 by 6
    Then the result should be 24

  Scenario: Divide two numbers
    Given a calculator
    When I divide 15 by 3
    Then the result should be 5
