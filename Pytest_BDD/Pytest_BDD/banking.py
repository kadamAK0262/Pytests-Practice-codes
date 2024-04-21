class Account:
    accounts = {}
 
    @classmethod
    def create_account(cls, balance):
        account_id = len(cls.accounts) + 1
        cls.accounts[account_id] = balance
 
    @classmethod
    def transfer_funds(cls, amount):
        cls.accounts[1] -= amount
        cls.accounts[2] += amount
 
    @classmethod
    def get_balance(cls, account_id):
        return cls.accounts.get(account_id, 0)