from pytest_bdd import given, when, then, scenario
from banking import Account
 
@scenario('banking.feature', 'Transfer funds between accounts')
def test_transfer_funds():
    pass
 
@given("I have an account with balance $1000")
def create_account_with_balance_1000():
    Account.create_account(balance=1000)
 
@given("I have another account with balance $500")
def create_second_account_with_balance_500():
    Account.create_account(balance=500)
 
@when("I transfer $300 from the first account to the second account")
def transfer_funds():
    Account.transfer_funds(300)
 
@then("the balance of the first account should be $700")
def check_first_account_balance():
    assert Account.get_balance(1) == 700
 
@then("the balance of the second account should be $800")
def check_second_account_balance():
    assert Account.get_balance(2) == 800