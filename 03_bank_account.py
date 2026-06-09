# ============================================
# Topic   : Encapsulation
# Question: Create a BankAccount class where
#           _balance is protected. Provide a
#           deposit method and get_balance method,
#           but prevent direct external modification.
# ============================================

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


account = BankAccount(1000)

account.deposit(500)
print(account.get_balance())   # Output: 1500

# Direct modification is discouraged
# account._balance = 9999  (bad practice - should not do this)
