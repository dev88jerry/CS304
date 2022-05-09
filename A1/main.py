"""
main to run bank account class
"""

from BankAccount import BankAccount
from ChequingAccount import ChequingAccount
from SavingsAccount import SavingsAccount

if __name__ == '__main__':
    myAccount = BankAccount("Jerry", "Rbc")
    savAccount = SavingsAccount("Jerry", "TD", 0.025)
    cheqAccount = ChequingAccount("Jerry", "BN", 1)

    myAccount.deposit(1000)
    myAccount.withdraw(10)
    savAccount.deposit(myAccount.get_balance())
    savAccount.accrue_interest()
    cheqAccount.deposit(savAccount.get_balance())
    cheqAccount.make_purchase(12)
    cheqAccount.make_purchase(1.01)
    myAccount += 100
    myAccount -= 10.1
    savAccount += myAccount.get_balance()
    savAccount.accrue_interest()
    cheqAccount += savAccount.get_balance()

    print("Values on accounts:")
    print(myAccount.get_balance())
    print(savAccount.get_balance())
    print(cheqAccount.get_balance())



