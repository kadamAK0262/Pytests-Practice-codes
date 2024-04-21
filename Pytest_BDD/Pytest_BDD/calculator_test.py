from pytest_bdd import scenarios, given, when, then
from calculator import Calculator

# Define your BDD scenarios
scenarios('calculator.feature')

# Fixture to instantiate the calculator
@given('a calculator')
def calculator():
    return Calculator()

# Step definitions
@when('I add 5 and 7')
def step_add_numbers(calculator):
    calculator.add(5, 7)

@then('the result should be 12')
def step_result_add(calculator):
    assert calculator.result == 12

@when('I subtract 7 from 12')
def step_subtract_numbers(calculator):
    calculator.subtract(12, 7)

@then('the result should be 5')
def step_result_subtract(calculator):
    assert calculator.result == 5

@when('I multiply 4 by 6')
def step_multiply_numbers(calculator):
    calculator.multiply(4, 6)

@then('the result should be 24')
def step_result_multiply(calculator):
    assert calculator.result == 24

@when('I divide 15 by 3')
def step_divide_numbers(calculator):
    calculator.divide(15, 3)

@then('the result should be 5')
def step_result_divide(calculator):
    assert calculator.result == 5
