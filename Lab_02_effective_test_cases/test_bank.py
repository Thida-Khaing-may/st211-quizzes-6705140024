# from bank import BankAccount
# def test_deposit_increases_balance():
#     account = BankAccount(balance=100)
#     new_balance = account.deposit(50)
#     assert new_balance == 150
# def test_everything_at_once():
#     account = BankAccount(100)
#     account.deposit(50)
#     account.withdraw(30)
#     account.deposit(10)
#     assert account.balance == 130

from  bank import BankAccount
shared_account = BankAccount(100)
def test_a_deposit():
    shared_account.deposit(50)
    assert shared_account.balance == 150
def test_b_withdraw():
    shared_account.withdraw(30)
    assert shared_account.balance == 120

#Arrange - Set up what we need:
#Act - Perform the action we want to test
#Assert - Check the expected result