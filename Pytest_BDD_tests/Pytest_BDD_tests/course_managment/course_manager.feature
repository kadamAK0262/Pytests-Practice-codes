Feature: Course Management

  Scenario: Create a new course
    Given a course manager
    When I create a course named "History"
    Then the course "History" should exist

  Scenario: Enroll a student in a course
    Given a course manager
    And a course named "Math"
    When I enroll the student "Alice" in the course "Math"
    Then "Alice" should be enrolled in the course "Math"
    And "Math" should have "Alice" as a student

  Scenario: Enroll multiple students in a course
    Given a course manager
    And a course named "Biology"
    When I enroll the students "Bob" and "Charlie" in the course "Biology"
    Then "Bob" should be enrolled in the course "Biology"
    And "Charlie" should be enrolled in the course "Biology"
    And "Biology" should have "Bob" and "Charlie" as students

  Scenario: Enroll a student in a non-existent course
    Given a course manager
    When I enroll the student "Dave" in the course "Physics"
    Then an error should be raised